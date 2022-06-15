import idenfy
import pop3
import smtp
import sys

from PyQt5.QtWidgets import QMessageBox,QLineEdit,QApplication,QMainWindow,QAbstractItemView,QTableWidgetItem,QFileDialog
import _thread
from PyQt5.QtCore import QCoreApplication
import poplib
import base64
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import datetime
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from PyQt5 import QtCore
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
import os.path




is_Idenfy = False

user = {
    'pop3':None,
    'user':None,
    'pass':None
}
class Email_Server(object):
    def __init__(self,user_dic):
        # print(user_dic)
        self.user_mail = user_dic['user']
        self.password = user_dic['pass']
        self.pop_server = user_dic['pop3'] # pop.163.com
        self.Connect_Server()

    def Connect_Server(self):
        # 连接服务
        self.server = poplib.POP3(self.pop_server)
        self.server.user(self.user_mail)
        self.server.pass_(self.password)

    def _close_(self):
        # 关闭服务器资源
        self.server.close()

    def Get_Email_Count(self):
        # 获取邮件数目
        email_num, email_size = self.server.stat()
        # print("邮件数量: {0}, 消息大小：{1}Byte".format(email_num,email_size))
        return email_num

    def Get_Email_Data(self,email_row = None):
        rsp, msglines, msgsiz = self.server.retr(email_row)
        # print("服务器的响应: {0},\n原始邮件内容： {1},\n该封邮件所占字节大小： {2}".format(rsp, msglines, msgsiz))
        # 解析
        msg_content = b'\r\n'.join(msglines).decode('gbk')
        # print(msg_content)
        msg = Parser().parsestr(text=msg_content)
        # print(msg)
        self.msg = msg

        # 标题
        subject = self.msg['Subject']
        value, charset = decode_header(subject)[0]
        if charset:
            value = value.decode(charset)
        self.email_title = value
        print("标题： ",self.email_title)

        # 发送方
        hdr, addr = parseaddr(self.msg['From'])
        name, charset = decode_header(hdr)[0]
        if charset:
            name = name.decode(charset)
        self.email_name = name
        self.email_addr = addr
        print("发送方: ",name,addr)

        # 时间
        date = decode_header(self.msg.get('date'))
        utcstr = date[0][0].replace('+00:00', '')
        self.email_time = str(utcstr)
        # print(utcdatetime)

        # 内容
        try:
            content = self.msg.get_payload()
            content_charset = content[0].get_content_charset()  # 获取编码格式
            print(content_charset)
            text = content[0].as_string().split('base64')[-1]
            try:
                text_content = base64.b64decode(text).decode(content_charset)  # base64解码
            except:
                text_content = base64.b64decode(text).decode('gbk','ignore')  # base64解码
            # print(text_content)
            self.content = text_content
        except:
            self.content = " "




mail_Server = None
fname=""
cfile=0
class Send_email(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.send_ui = smtp.Ui_MainWindow()
        self.send_ui.setupUi(self)
        self.send_ui.pushButton_2.clicked.connect(self.close)
        self.send_ui.pushButton.clicked.connect(self.Send)
        self.send_ui.ffliechose.clicked.connect(self.showDialog)

    def showDialog(self):
        global fname
        global cfile
        fname = QFileDialog.getOpenFileName(self, 'Open file', '.')
        self.send_ui.choosefile.setText(os.path.basename(fname[0]))
        cfile=1
        print(fname[0])
        print(os.path.basename(fname[0]))
        
    def Send(self):
        global mail_Server
        try:
            smtp_server = "smtp."+mail_Server.user_mail[mail_Server.user_mail.find("@")+1:]
            smtp_port ="465"
            send_name = self.send_ui.lineEdit_4.text()
            recv_mail = self.send_ui.lineEdit_5.text()
            send_title = self.send_ui.lineEdit_6.text()
            send_text = self.send_ui.textEdit.toPlainText()
        except:
            QMessageBox.about(self, "Message", "填写完整信息")
        _thread.start_new_thread(self.Send_Email, (smtp_server,smtp_port,send_name,recv_mail,send_title,send_text,))

    def Send_Email(self,smtp_server,smtp_port,send_name,recv_mail,send_title,send_text):
        global mail_Server
        try:
            content = MIMEText(send_text,'plain','utf-8')
            msg = MIMEMultipart()
            msg.attach(content)
            global fname
            if(cfile):
                with open(fname[0], 'rb') as f:
    # 设置MIMEBase对象包装附件
                    attachment = MIMEBase('application', 'octet-stream')
    # 添加附件
                    attachment.set_payload(f.read())
    # 添加附件标题
                    attachment.add_header('Content-Disposition', 'attachment', filename=('gbk', '', os.path.basename(fname[0])))
    # 编码附件
                    encoders.encode_base64(attachment)
    # 添加附件到邮件中
                    msg.attach(attachment)
 
            msg['From'] = formataddr([send_name,mail_Server.user_mail])#发件人邮箱昵称、发件人邮箱
            msg['To'] = formataddr(["川大", recv_mail])  # 收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = send_title  # 邮件主题（标题
            server = smtplib.SMTP_SSL(smtp_server, int(smtp_port))  # 发送人邮箱SMTP服务器，端口号
            server.login(mail_Server.user_mail, mail_Server.password)  # 发件人邮箱账号、密码
            server.sendmail(mail_Server.user_mail, [recv_mail, ], msg.as_string())
            server.quit()
            #QMessageBox.about(self, "Message", "发送成功！")
            self.send_ui.yes.setText("发送成功！！！！")
            
        except:
           # QMessageBox.critical(self, "失败", "pop验证失败", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            self.send_ui.yes.setText("发送失败，SMTP或邮箱错误")



sendUi = None

class mainWin(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = pop3.Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.main_ui.pushButton_2.clicked.connect(self.Send)
        self.main_ui.pushButton_4.clicked.connect(self.Update)
        self.main_ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.main_ui.tableWidget.itemClicked.connect(self.itemclick)
        self.main_ui.textEdit.document().setMaximumBlockCount(100)

    def itemclick(self):
        # print("哈哈哈nb")
        now_current_row = self.main_ui.tableWidget.currentIndex().row()
        print(now_current_row)
        rowtitle = self.main_ui.tableWidget.item(now_current_row,0).text()
        # print(rowdata)
        rowsender = self.main_ui.tableWidget.item(now_current_row,1).text()
        etime = self.main_ui.tableWidget.item(now_current_row,2).text()
        rowaddr = self.main_ui.tableWidget.item(now_current_row,3).text()
        contents = self.main_ui.tableWidget.item(now_current_row,4).text()
        self.main_ui.textEdit.clear()
        self.main_ui.lineEdit.clear()
        self.main_ui.lineEdit_2.clear()
        self.main_ui.lineEdit_3.clear()
        self.main_ui.lineEdit_4.clear()
        self.main_ui.lineEdit.setText(rowtitle)
        self.main_ui.lineEdit_2.setText(rowsender)
        self.main_ui.lineEdit_3.setText(rowaddr)
        self.main_ui.lineEdit_4.setText(etime)
        if len(contents) > 5000:
            self.main_ui.textEdit.append(" ")
        else:
           self.main_ui.textEdit.append(contents)

    def Update(self):
        global is_Idenfy,mail_Server
        if not is_Idenfy:
            QMessageBox.about(self, "Message", "请先登录")
        else:
            _thread.start_new_thread(self.Upthread, ())

    def Upthread(self):
        global mail_Server
        #清空列表
        allrownum = self.main_ui.tableWidget.rowCount()
        for i in range(allrownum):
            self.main_ui.tableWidget.removeRow(0)
        # 获取邮箱邮件数
        mail_count = mail_Server.Get_Email_Count()
    
        if(mail_count>10):
            for i in range(mail_count,mail_count-10,-1):
                mail_Server.Get_Email_Data(i)
                _thread.start_new_thread(self.Display, (mail_Server.email_title,mail_Server.email_name,mail_Server.email_addr,mail_Server.content,mail_Server.email_time,))
        else:
            for i in range(mail_count,0,-1):
                mail_Server.Get_Email_Data(i)
                _thread.start_new_thread(self.Display, (mail_Server.email_title,mail_Server.email_name,mail_Server.email_addr,mail_Server.content,mail_Server.email_time,))

    def Display(self,title,name,addr,content,etime):
        rrow = self.main_ui.tableWidget.rowCount()
        self.main_ui.tableWidget.insertRow(rrow)
        self.main_ui.tableWidget.setItem(rrow, 0, QTableWidgetItem(title))
        self.main_ui.tableWidget.setItem(rrow, 1, QTableWidgetItem(name))
        self.main_ui.tableWidget.setItem(rrow, 2, QTableWidgetItem(str(etime)))
        self.main_ui.tableWidget.setItem(rrow, 3, QTableWidgetItem(addr))
        self.main_ui.tableWidget.setItem(rrow, 4, QTableWidgetItem(content))

    def Send(self):
        global is_Idenfy,user,sendUi
        if not is_Idenfy:
            QMessageBox.about(self, "Message", "请先登录")
        else:
            sendUi = Send_email()
            sendUi.send_ui.label_8.setText(user['user'])
            sendUi.show()


class loginWin(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.login_ui = idenfy.Ui_MainWindow()
        self.login_ui.setupUi(self)
        self.login_ui.pushButton_2.clicked.connect(self.close)
        self.login_ui.pushButton.clicked.connect(self.Login)
        self.login_ui.lineEdit_2.setEchoMode(QLineEdit.Password)

    def Login(self):
        print("login....")
        global user,mail_Server,is_Idenfy
        user['user'] = str(self.login_ui.lineEdit.text())
        user['pass'] = str(self.login_ui.lineEdit_2.text())
        #user['pop3'] = str(self.login_ui.lineEdit_3.text())
        user['pop3'] = "pop."+user['user'][user['user'].find("@")+1:]
        # print(user)
        try:
            mail_Server =Email_Server(user)
            print("连接成功.......")
            QMessageBox.about(self, "连接成功", "验证成功！")
      
            is_Idenfy = True
            
            self.close()
            
        except:
            print("pop验证失败！")
            QMessageBox.critical(self, "失败", "pop验证失败", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)


if __name__ == '__main__':
    
   
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    
   
    ui = mainWin()
    loginui = loginWin()
    ui.main_ui.pushButton.clicked.connect(loginui.show)
    ui.main_ui.pushButton_3.clicked.connect(QApplication.quit)
    ui.show()

    sys.exit(app.exec_())