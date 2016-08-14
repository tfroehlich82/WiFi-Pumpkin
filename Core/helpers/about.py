from Core.loaders.Stealth.PackagesUI import *

class License(QTextEdit):
    def __init__(self,parent = None):
        super(License,self).__init__(parent)
        self.setReadOnly(True)
        self.setWindowTitle('License WiFI-Pumpkin GPL')
        self.setGeometry(0,0,300,300)
        self.center()
        self.setText(open('LICENSE','r').read())
    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

class ChangeLog(QTextEdit):
    def __init__(self,parent = None):
        super(ChangeLog,self).__init__(parent)
        self.setMinimumHeight(240)
        self.setStyleSheet('''QWidget {
        color: #b1b1b1; background-color: #323232;}''')
        self.setText(open('CHANGELOG','r').read())
        self.setReadOnly(True)


class SettingsTranks(QVBoxLayout):
    def __init__(self,parent = None):
        super(SettingsTranks, self).__init__(parent)
        self.mainLayout    = QFormLayout()
        self.scrollwidget = QWidget()
        self.scrollwidget.setLayout(self.mainLayout)
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.scrollwidget)

        self.formMode = QFormLayout()
        self.formMode.addRow(QLabel('<a href="https://github.com/xtr4nge"><strong>@xtr4nge</strong></a>'))
        self.formMode.addRow(QLabel('Sslstrip2 based version fork<br><br>'))
        self.formMode.addRow(QLabel('<a href="https://github.com/LeonardoNve"><strong>@LeonardoNve</strong></a>'))
        self.formMode.addRow(QLabel('Plugin SSLstrip version fork,Plugin dns2proxy<br><br>'))
        self.formMode.addRow(QLabel('<a href="https://github.com/supernothing"><strong>Ben Schmidt @supernothing</strong></a>'))
        self.formMode.addRow(QLabel('Plugin Sergio Proxy - bypass HSTS<br><br>'))
        self.formMode.addRow(QLabel('<a href="https://github.com/DanMcInerney"><strong>Dan McInerney @danhmcinerney</strong></a>'))
        self.formMode.addRow(QLabel('Plugin Netcreds - Sniffs sensitive data<br><br>'))
        self.formMode.addRow(QLabel('<a href="http://www.yasinuludag.com/darkorange.stylesheet"><strong>Yasin Uludag</strong></a>'))
        self.formMode.addRow(QLabel('theme1.qss - Qt dark orange stylesheet<br><br>'))
        self.formMode.addRow(QLabel('<a href="https://github.com/ColinDuquesnoy/QDarkStyleSheet"><strong>Colin Duquesnoy @ColinDuquesnoy</strong></a>'))
        self.formMode.addRow(QLabel('theme2.qss - Qt dark blue stylesheet<br><br>'))
        self.mainLayout.addRow(self.formMode)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.scroll)
        self.addLayout(self.layout)

class frmAbout(PumpkinModule):
    def __init__(self,author,emails,version,
        update,license,desc, parent = None):
        super(frmAbout, self).__init__(parent)
        self.author      = author
        self.emails      = emails
        self.version     = version
        self.update      = update
        self.desc        = QLabel(desc[0]+'<br>')
        self.setWindowTitle("About WiFi-Pumpkin")
        self.Main = QVBoxLayout()
        self.frm = QFormLayout()
        self.setGeometry(0, 0, 350, 400)
        self.center()
        self.loadtheme(self.configure.XmlThemeSelected())
        self.Qui_update()

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def Qui_update(self):
        self.logoapp = QLabel('')
        self.logoapp.setPixmap(QPixmap('Icons/icon.ico').scaled(96,96))
        self.form = QFormLayout()
        self.form2 = QHBoxLayout()
        self.form.addRow(self.logoapp,QLabel(
        QString('<h2>WiFi-Pumpkin {}</h2>'.format(self.version))))
        self.tabwid = QTabWidget(self)
        self.TabAbout = QWidget(self)
        self.TabVersion = QWidget(self)
        self.TabTranks  = QWidget()
        self.TabChangelog = QWidget(self)
        self.btn_exit = QPushButton("Close")
        self.btn_exit.setFixedWidth(90)
        self.btn_exit.setIcon(QIcon('Icons/cancel.png'))
        self.btn_exit.clicked.connect(self.close)

        self.formAbout = QFormLayout()
        self.formVersion = QFormLayout()
        self.formTranks = QFormLayout()
        self.formChange = QFormLayout()

        # About section
        self.formAbout.addRow(self.desc)
        self.formAbout.addRow(QLabel('Last Update:'))
        self.formAbout.addRow(QLabel(self.update+'<br>'))
        self.formAbout.addRow(QLabel('Feedback:'))
        self.formAbout.addRow(QLabel(self.emails[0]))
        self.formAbout.addRow(QLabel(self.emails[1]+'<br>'))
        self.formAbout.addRow(QLabel('Copyright 2015-2016, '+self.author[:-14]))
        self.gnu = QLabel('<a href="link">License: GNU General Public License Version</a><br>')
        self.gnu.linkActivated.connect(self.link)
        self.formAbout.addRow(self.gnu)
        self.formAbout.addRow(QLabel('<center>{}</center>'.format(self.author[-14:])))
        self.TabAbout.setLayout(self.formAbout)

        # Version Section
        self.formVersion.addRow(QLabel('<strong>Version: {}</strong><br>'.format(self.version)))
        self.formVersion.addRow(QLabel('Using:'))
        import platform
        python_version = platform.python_version()
        self.formVersion.addRow(QLabel('''
        <ul>
          <li>QTVersion: {}</li>
          <li>Python: {}</li>
        </ul>'''.format(QT_VERSION_STR,python_version)))
        self.TabVersion.setLayout(self.formVersion)

        # Tranks Section
        self.TabpageTranks = QVBoxLayout(self.TabTranks)
        self.formTE = SettingsTranks()
        self.TabpageTranks.addLayout(self.formTE)

        # Changelog Section
        self.formChange.addRow(ChangeLog())
        self.TabChangelog.setLayout(self.formChange)

        # self.form.addRow(self.btn_exit)
        self.tabwid.addTab(self.TabAbout,'About')
        self.tabwid.addTab(self.TabVersion,'Version')
        self.tabwid.addTab(self.TabChangelog,'ChangeLog')
        self.tabwid.addTab(self.TabTranks,'TranksTo')
        self.form.addRow(self.tabwid)
        self.form2.addSpacing(240)
        self.form2.addWidget(self.btn_exit)
        self.form.addRow(self.form2)
        self.Main.addLayout(self.form)
        self.setLayout(self.Main)

    def link(self):
        self.formLicense = License()
        self.formLicense.show()
