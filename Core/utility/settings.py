from re import search
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Core.utility.collection import SettingsINI

"""
Description:
    This program is a module for wifi-pumpkin.py.

Copyright:
    Copyright (C) 2015-2016 Marcos Nesster P0cl4bs Team
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>
"""

class SettingsTabGeneral(QVBoxLayout):
    def __init__(self,Settings=None,parent= None):
        super(SettingsTabGeneral, self).__init__(parent)
        self.Settings      = Settings
        self.mainLayout    = QFormLayout()
        self.scrollwidget = QWidget()
        self.scrollwidget.setLayout(self.mainLayout)
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.scrollwidget)

        self.GruPag0=QButtonGroup()
        self.GruPag1=QButtonGroup()
        self.GruPag2=QButtonGroup()
        self.GruPag3=QButtonGroup()
        self.GruPag4=QButtonGroup()

        # group options
        self.groupAP = QGroupBox()
        self.groupDhcp = QGroupBox()
        self.groupDeauth = QGroupBox()
        self.groupScan   = QGroupBox()
        self.groupThemes = QGroupBox()

        #form group
        self.formGroupAP = QFormLayout()
        self.formGroupDHCP = QFormLayout()
        self.formGroupDeauth = QFormLayout()
        self.formGroupScan = QFormLayout()
        self.formGroupThemes = QFormLayout()

        # set layout into groupbox
        self.groupAP.setLayout(self.formGroupAP)
        self.groupDhcp.setLayout(self.formGroupDHCP)
        self.groupDeauth.setLayout(self.formGroupDeauth)
        self.groupScan.setLayout(self.formGroupScan)
        self.groupThemes.setLayout(self.formGroupThemes)

        self.groupAP.setTitle('Access Point:')
        self.groupDhcp.setTitle('DHCP:')
        self.groupDeauth.setTitle('Deauth:')
        self.groupScan.setTitle('Scan devices:')
        self.groupThemes.setTitle('Pumpkin Themes:')

        #page general
        self.Apname =  QLineEdit()
        self.Apname.setFixedWidth(80)
        self.channel = QSpinBox()

        self.AP_0 = QRadioButton('hostapd')
        self.AP_1 = QRadioButton('airbase-ng')
        self.AP_1.setEnabled(False)
        self.d_scapy = QRadioButton('Scapy Deauth')
        self.d_mdk = QRadioButton('mdk3 Deauth')
        self.scan_scapy = QRadioButton('Scan from scapy')
        self.scan_airodump = QRadioButton('Scan from airodump-ng')
        self.dhcp1 = QRadioButton('iscdhcpserver')
        self.dhcp2 = QRadioButton('dnsmasq')
        self.dhcp2.setDisabled(True)
        self.theme1 = QRadioButton('theme Dark Orange')
        self.theme2 = QRadioButton('theme Dark blue')

        #grup page 1
        self.GruPag0.addButton(self.AP_0)
        self.GruPag0.addButton(self.AP_1)
        self.GruPag1.addButton(self.d_scapy)
        self.GruPag1.addButton(self.d_mdk)
        self.GruPag2.addButton(self.dhcp1)
        self.GruPag2.addButton(self.dhcp2)
        self.GruPag3.addButton(self.scan_scapy)
        self.GruPag3.addButton(self.scan_airodump)
        self.GruPag4.addButton(self.theme1)
        self.GruPag4.addButton(self.theme2)

        #page 1
        self.Apname.setText(self.Settings.get_setting('accesspoint','APname'))
        self.channel.setValue(int(self.Settings.get_setting('accesspoint','channel')))
        self.AP_check = self.Settings.get_setting('accesspoint','using')
        self.deauth_check = self.Settings.get_setting('settings','deauth')
        self.scan_AP_check = self.Settings.get_setting('settings','scanner_AP')
        self.dhcp_check = self.Settings.get_setting('accesspoint', 'dhcp_server')
        self.theme_selected = self.Settings.get_setting('settings','themes')

        # setting page 1
        if self.AP_check == 'hostapd': self.AP_0.setChecked(True)
        if self.deauth_check == 'packets_mdk3':
            self.d_mdk.setChecked(True)
        else:
            self.d_scapy.setChecked(True)
        if self.dhcp_check == 'iscdhcpserver':
            self.dhcp1.setChecked(True)
        else:
            self.dhcp2.setChecked(True)
        if self.scan_AP_check == 'scan_scapy':
            self.scan_scapy.setChecked(True)
        else:
            self.scan_airodump.setChecked(True)
        if self.theme_selected == 'themes/theme1':
            self.theme1.setChecked(True)
        else:
            self.theme2.setChecked(True)
        self.formGroupAP.addRow('AP Name:',self.Apname)
        self.formGroupAP.addRow('Channel:',self.channel)
        self.formGroupAP.addRow(self.AP_0)
        self.formGroupAP.addRow(self.AP_1)
        self.formGroupDeauth.addRow(self.d_scapy)
        self.formGroupDeauth.addRow(self.d_mdk)
        self.formGroupScan.addRow(self.scan_scapy)
        self.formGroupScan.addRow(self.scan_airodump)
        self.formGroupDHCP.addRow(self.dhcp1)
        self.formGroupDHCP.addRow(self.dhcp2)
        self.formGroupThemes.addRow(self.theme1)
        self.formGroupThemes.addRow(self.theme2)

        self.mainLayout.addRow(self.groupAP)
        self.mainLayout.addRow(self.groupDhcp)
        self.mainLayout.addRow(self.groupScan)
        self.mainLayout.addRow(self.groupDeauth)
        self.mainLayout.addRow(self.groupThemes)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.scroll)
        self.addLayout(self.layout)


class frm_Settings(QDialog):
    def __init__(self, parent = None):
        super(frm_Settings, self).__init__(parent)
        self.setWindowTitle('Settings WiFi-Pompkin')
        self.Settings = SettingsINI('Core/config/app/config.ini')
        self.loadtheme(self.XmlThemeSelected())
        self.setGeometry(0, 0, 420, 440)
        self.center()
        self.Qui()

    def loadtheme(self,theme):
        sshFile=("Core/%s.qss"%(theme))
        with open(sshFile,"r") as fh:
            self.setStyleSheet(fh.read())

    def XmlThemeSelected(self):
        return self.Settings.get_setting('settings','themes')

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def save_settings(self):
        if self.pageTab1.d_scapy.isChecked():
            self.Settings.set_setting('settings','deauth','packets_scapy')
        elif self.pageTab1.d_mdk.isChecked():
            self.Settings.set_setting('settings','deauth','packets_mdk3')
        if self.pageTab1.scan_scapy.isChecked():
            self.Settings.set_setting('settings','scanner_AP','scan_scapy')
        elif self.pageTab1.scan_airodump.isChecked():
            self.Settings.set_setting('settings','scanner_AP','scan_airodump')
        if self.pageTab1.dhcp1.isChecked():
            self.Settings.set_setting('accesspoint','dhcp_server','iscdhcpserver')
        if self.pageTab1.theme1.isChecked():
            self.Settings.set_setting('settings','themes','themes/theme1')
        elif self.pageTab1.theme2.isChecked():
            self.Settings.set_setting('settings','themes','themes/theme2')
        if self.scan1.isChecked():
            self.Settings.set_setting('settings','Function_scan','Ping')
        elif self.scan2.isChecked():
            self.Settings.set_setting('settings','Function_scan','Nmap')

        self.Settings.set_setting('settings','mdk3',str(self.txt_arguments.text()))
        self.Settings.set_setting('settings','scanner_rangeIP',str(self.txt_ranger.text()))
        self.Settings.set_setting('accesspoint','APname', str(self.pageTab1.Apname.text()))
        self.Settings.set_setting('accesspoint','channel', str(self.pageTab1.channel.value()))
        self.Settings.set_setting('settings','redirect_port', str(self.redirectport.text()))
        with open('Core/config/hostapd/hostapd+.conf','w') as apconf:
            apconf.write(self.ListHostapd.toPlainText())
        self.close()


    def listItemclicked(self,pos):
        item = self.ListRules.selectedItems()
        self.listMenu= QMenu()
        menu = QMenu()
        additem = menu.addAction('Add')
        editem = menu.addAction('Edit')
        removeitem = menu.addAction('Remove ')
        clearitem = menu.addAction('clear')
        action = menu.exec_(self.ListRules.viewport().mapToGlobal(pos))
        if action == removeitem:
            if item != []:
                self.ListRules.takeItem(self.ListRules.currentRow())
        elif action == additem:
            text, resp = QInputDialog.getText(self, 'Add rules iptables',
            'Enter the rules iptables:')
            if resp:
                try:
                    itemsexits = []
                    for index in xrange(self.ListRules.count()):
                        itemsexits.append(str(self.ListRules.item(index).text()))
                    for i in itemsexits:
                        if search(str(text),i):
                            QMessageBox.information(self,'Rules exist','this rules already exist!')
                            return
                    item = QListWidgetItem()
                    item.setText(text)
                    item.setSizeHint(QSize(30,30))
                    self.ListRules.addItem(item)
                except Exception as e:
                    QMessageBox.information(self,'error',str(e))
                    return
        elif action == editem:
            text, resp = QInputDialog.getText(self, 'Add rules iptables',
            'Enter the rules iptables:',text=self.ListRules.item(self.ListRules.currentRow()).text())
            if resp:
                try:
                    itemsexits = []
                    for index in xrange(self.ListRules.count()):
                        itemsexits.append(str(self.ListRules.item(index).text()))
                    for i in itemsexits:
                        if search(str(text),i):
                            QMessageBox.information(self,'Rules exist','this rules already exist!')
                            return
                    item = QListWidgetItem()
                    item.setText(text)
                    item.setSizeHint(QSize(30,30))
                    self.ListRules.insertItem(self.ListRules.currentRow(),item)
                except Exception as e:
                    QMessageBox.information(self,'error',str(e))
                    return
        elif action == clearitem:
            self.ListRules.clear()

    def redirectAP(self):
        item = QListWidgetItem()
        if self.check_redirect.isChecked():
            item.setText('iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 10.0.0.1:80')
            item.setSizeHint(QSize(30,30))
            self.ListRules.addItem(item)
            return
        rules = []
        for index in xrange(self.ListRules.count()):
            rules.append(str(self.ListRules.item(index).text()))
        for i,j in enumerate(rules):
            if search('--to-destination 10.0.0.1:80',j):
                self.ListRules.takeItem(i)
    def Qui(self):
        self.Main = QVBoxLayout()
        self.formGroupAd  = QFormLayout()
        self.form = QFormLayout()
        self.tabcontrol = QTabWidget()

        # tabs
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()

        self.page_1 = QVBoxLayout(self.tab1)
        self.page_2 = QFormLayout(self.tab2)
        self.page_3 = QFormLayout(self.tab3)
        self.page_4 = QFormLayout(self.tab4)

        self.tabcontrol.addTab(self.tab1, 'General')
        self.tabcontrol.addTab(self.tab2, 'Advanced')
        self.tabcontrol.addTab(self.tab3,'Iptables')
        self.tabcontrol.addTab(self.tab4,'hostpad')

        self.pageTab1 = SettingsTabGeneral(self.Settings)
        self.page_1.addLayout(self.pageTab1)

        self.groupAdvanced = QGroupBox()
        self.groupAdvanced.setTitle('Advanced Settings:')
        self.groupAdvanced.setLayout(self.formGroupAd)

        self.btn_save = QPushButton('Save')
        self.btn_save.clicked.connect(self.save_settings)
        self.btn_save.setFixedWidth(80)
        self.btn_save.setIcon(QIcon('Icons/Save.png'))


        #page Adavanced
        self.txt_ranger = QLineEdit(self)
        self.txt_arguments = QLineEdit(self)
        self.scan1 = QRadioButton('Ping Scan:: Very fast scan IP')
        self.scan2 = QRadioButton('Python-Nmap:: Get hostname from IP')
        self.redirectport = QLineEdit(self)

        # page Iptables
        self.ListRules = QListWidget(self)
        self.ListRules.setFixedHeight(300)
        self.ListRules.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ListRules.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ListRules.connect(self.ListRules,
        SIGNAL('customContextMenuRequested(QPoint)'),
        self.listItemclicked)
        for ech in self.Settings.get_all_childname('iptables'):
            item = QListWidgetItem()
            item.setText(self.Settings.get_setting('iptables',ech))
            item.setSizeHint(QSize(30,30))
            self.ListRules.addItem(item)

        # page hostpad
        self.ListHostapd = QTextEdit(self)
        self.ListHostapd.setFixedHeight(300)
        with open('Core/config/hostapd/hostapd+.conf','r') as apconf:
            self.ListHostapd.setText(apconf.read())

        # grup page 2
        self.gruButtonPag2 = QButtonGroup()
        self.gruButtonPag2.addButton(self.scan1)
        self.gruButtonPag2.addButton(self.scan2)

        self.txt_ranger.setText(self.Settings.get_setting('settings','scanner_rangeIP'))
        self.txt_arguments.setText(self.Settings.get_setting('settings','mdk3'))
        self.scanIP_selected  = self.Settings.get_setting('settings','Function_scan')

        if self.scanIP_selected == 'Ping': self.scan1.setChecked(True)
        self.scan2.setEnabled(False)
        #settings tab Advanced
        self.redirectport.setText(self.Settings.get_setting('settings','redirect_port'))

        #add tab Advanced
        self.formGroupAd.addRow(QLabel('Thread Scan IP-Address:'))
        self.formGroupAd.addRow(self.scan1)
        self.formGroupAd.addRow(self.scan2)
        self.formGroupAd.addRow('Port sslstrip:',self.redirectport)
        self.formGroupAd.addRow(QLabel('mdk3 Args:'),self.txt_arguments)
        self.formGroupAd.addRow(QLabel('Range Scanner:'),self.txt_ranger)
        self.page_2.addRow(self.groupAdvanced)

        #add tab iptables
        self.page_3.addWidget(QLabel('Iptables:'))
        self.page_3.addRow(self.ListRules)

        #add tab hostpad
        self.page_4.addWidget(QLabel('Settings hostapd:'))
        self.page_4.addRow(self.ListHostapd)

        self.form.addRow(self.tabcontrol)
        self.form.addRow(self.btn_save)
        self.Main.addLayout(self.form)
        self.setLayout(self.Main)
