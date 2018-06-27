#!/usr/bin/python
import pymssql
import requests
import json
import os, sys
import socket
import datetime
from flask import Flask, request, url_for, redirect, jsonify
from flask import render_template
from decimal import getcontext, Decimal

app = Flask(__name__)

ups_Life_A = ''
serialName_A = ''
systemMode_A = 0
inputLine_A = 0
inputFreq_A = 0
inputVolt_A = 0
outputLine_A = 0
outputFreq_A = 0
outputVolt_A = 0
outputWatt_A = 0
outputAmp_A = 0
outputPercent_A = 0
batteryHealth_A = ''
batteryStatus_A = ''
batteryCharge_Mode_A = ''
batteryRemain_Min_A = ''
batteryRemain_Sec_A = ''
batteryVolt_A = 0
batteryTemp_A = 0
batteryRemain_Percent_A = 0
lastBattery_Year_A = 0
lastBattery_Mon_A = 0
lastBattery_Day_A = 0
nextBattery_Year_A = 0
nextBattery_Mon_A = 0
nextBattery_Day_A = 0
ups_Life_B = ''
serialName_B = ''
systemMode_B = 0
inputLine_B = 0
inputFreq_B = 0
inputVolt_B = 0
outputLine_B = 0
outputFreq_B = 0
outputVolt_B = 0
outputWatt_B = 0
outputAmp_B = 0
outputPercent_B = 0
batteryHealth_B = ''
batteryStatus_B = ''
batteryCharge_Mode_B = ''
batteryRemain_Min_B = ''
batteryRemain_Sec_B = ''
batteryVolt_B = 0
batteryTemp_B = 0
batteryRemain_Percent_B = 0
lastBattery_Year_B = 0
lastBattery_Mon_B = 0
lastBattery_Day_B = 0
nextBattery_Year_B = 0
nextBattery_Mon_B = 0
nextBattery_Day_B = 0
hostname = '10.0.0.197'					#chang to your service IP
port = '5000'							#chang to your service Port
hostHealth = ''
releaseTime = ''


@app.route('/')
def root():
	login_check = url_for('login')
	return redirect(login_check)

@app.route('/now/<user_id>', methods=['POST', 'GET'])
def index(user_id):
	if request.method == 'GET':
		conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
		cursor = conn.cursor()
		temp = "SELECT mId FROM member"
	#	print(temp)
		cursor.execute(temp)
		memberList = cursor.fetchall()
		conn.commit()
		cursor.close()
		tmp = ''
		for x in range(0, len(memberList)):
			tmp = ''
			for y in list(str(memberList[x]).split("'")[1]):
				if y != ' ':
				#	print('/' + y + '/')
					tmp = tmp + y
				else:
					break
			if tmp == user_id:
				conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
				cursor = conn.cursor()
				temp = "SELECT mIP FROM member WHERE mId = '" + user_id + "'"
			#	print(temp)
				cursor.execute(temp)
				ipList = cursor.fetchall()
				conn.commit()
				cursor.close()
				tmp = ''
				for z in list(str(ipList[0]).split("'")[1]):
					if z != ' ':
					#	print('/' + z + '/')
						tmp = tmp + z
					else:
						break
				if tmp == request.remote_addr:		
					print('Login IP :' + tmp)
					global releaseTime, hostname, port, hostHealth
					global serialName_A, systemMode_A, ups_Life_A, inputLine_A, inputFreq_A, inputVolt_A
					global outputLine_A, outputFreq_A, outputVolt_A, outputWatt_A, outputAmp_A, outputPercent_A
					global batteryHealth_A, batteryStatus_A, batteryCharge_Mode_A
					global batteryRemain_Min_A, batteryRemain_Sec_A, batteryVolt_A, batteryTemp_A, batteryRemain_Percent_A
					global lastBattery_Year_A, lastBattery_Mon_A, lastBattery_Day_A, nextBattery_Year_A, nextBattery_Mon_A, nextBattery_Day_A
					global serialName_B, systemMode_B, ups_Life_B,  inputLine_B, inputFreq_B, inputVolt_B
					global outputLine_B, outputFreq_B, outputVolt_B, outputWatt_B, outputAmp_B, outputPercent_B
					global batteryHealth_B, batteryStatus_B, batteryCharge_Mode_B
					global batteryRemain_Min_B, batteryRemain_Sec_B, batteryVolt_B, batteryTemp_B, batteryRemain_Percent_B
					global lastBattery_Year_B, lastBattery_Mon_B, lastBattery_Day_B, nextBattery_Year_B, nextBattery_Mon_B, nextBattery_Day_B
					localOS = os.system('uname 2>&1 >/var/tmp/os.txt')
					if(localOS == 0):
						response = os.system('ping -c 1 ' + hostname + ' 2>&1 >/var/tmp/ping.txt')
					else:
						response = os.system('ping -n 1 ' + hostname + ' 2>&1 >ping.txt')
					if response == 0:						# check network sevice & server is on
						sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						result = sock.connect_ex((hostname, int(port)))
						if result == 0:
							sock.close()
							releaseTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
							print ('Data Relaod : ', releaseTime)
							distance = 'http://' + hostname + ':' + port
							r = requests.get(distance)
							value = r.content.decode('utf-8')	# get return json value
					#		print(value)
							key = json.loads(value)
					#		print (json.dumps(key , sort_keys=True, indent=4, separators=(',', ': ')))	# show on the all split json format
					#		change the json key to local temp value
							ups_Life_A = key['ups_Life_A']
							serialName_A = key['connect_A']
							status_A = key['battery_A']['status']
							batteryHealth_A = status_A['batteryHealth_A']
							batteryStatus_A = status_A['batteryStatus_A']
							batteryCharge_Mode_A = status_A['batteryCharge_Mode_A']
							batteryRemain_Min_A = status_A['batteryRemain_Min_A']
							batteryRemain_Sec_A = status_A['batteryRemain_Sec_A']
							batteryVolt_A = status_A['batteryVolt_A']
							batteryTemp_A = status_A['batteryTemp_A']
							batteryRemain_Percent_A = status_A['batteryRemain_Percent_A']
							lastBattery_A = key['battery_A']['lastChange']
							nextBattery_A = key['battery_A']['nextChange']
							inputStatus_A = key['input_A']
							outputStatus_A = key['output_A']
							inputLine_A = inputStatus_A['inputLine_A']
							inputFreq_A = inputStatus_A['inputFreq_A']
							inputVolt_A = inputStatus_A['inputVolt_A']
							systemMode_A = outputStatus_A['systemMode_A']
							outputLine_A = outputStatus_A['outputLine_A']
							outputFreq_A = outputStatus_A['outputFreq_A']
							outputVolt_A = outputStatus_A['outputVolt_A']
							outputAmp_A = outputStatus_A['outputAmp_A']
							outputWatt_A = outputStatus_A['outputWatt_A']
							outputPercent_A = outputStatus_A['outputPercent_A']
							lastBattery_Year_A = lastBattery_A['lastBattery_Year_A']
							lastBattery_Mon_A = lastBattery_A['lastBattery_Mon_A']
							lastBattery_Day_A = lastBattery_A['lastBattery_Day_A']
							nextBattery_Year_A = nextBattery_A['nextBattery_Year_A']
							nextBattery_Mon_A = nextBattery_A['nextBattery_Mon_A']
							nextBattery_Day_A = nextBattery_A['nextBattery_Day_A']
							ups_Life_B = key['ups_Life_B']
							serialName_B = key['connect_B']
							status_B = key['battery_B']['status']
							batteryHealth_B = status_B['batteryHealth_B']
							batteryStatus_B = status_B['batteryStatus_B']
							batteryCharge_Mode_B = status_B['batteryCharge_Mode_B']
							batteryRemain_Min_B = status_B['batteryRemain_Min_B']
							batteryRemain_Sec_B = status_B['batteryRemain_Sec_B']
							batteryVolt_B = status_B['batteryVolt_B']
							batteryTemp_B = status_B['batteryTemp_B']
							batteryRemain_Percent_B = status_B['batteryRemain_Percent_B']
							lastBattery_B = key['battery_B']['lastChange']
							nextBattery_B = key['battery_B']['nextChange']
							inputStatus_B = key['input_B']
							outputStatus_B = key['output_B']
							inputLine_B = inputStatus_B['inputLine_B']
							inputFreq_B = inputStatus_B['inputFreq_B']
							inputVolt_B = inputStatus_B['inputVolt_B']
							systemMode_B = outputStatus_B['systemMode_B']
							outputLine_B = outputStatus_B['outputLine_B']
							outputFreq_B = outputStatus_B['outputFreq_B']
							outputVolt_B = outputStatus_B['outputVolt_B']
							outputAmp_B = outputStatus_B['outputAmp_B']
							outputWatt_B = outputStatus_B['outputWatt_B']
							outputPercent_B = outputStatus_B['outputPercent_B']
							lastBattery_Year_B = lastBattery_B['lastBattery_Year_B']
							lastBattery_Mon_B = lastBattery_B['lastBattery_Mon_B']
							lastBattery_Day_B = lastBattery_B['lastBattery_Day_B']
							nextBattery_Year_B = nextBattery_B['nextBattery_Year_B']
							nextBattery_Mon_B = nextBattery_B['nextBattery_Mon_B']
							nextBattery_Day_B = nextBattery_B['nextBattery_Day_B']
							hostHealth = 'Alive'
						else:
							print ('http://' + hostname +':' + port + ' Service Port Found !')
							hostHealth = 'Port-Error'
					else:
						print ('http://', hostname, ' Server IP Not Found !')
						hostHealth = 'IP-Error'
					return render_template('mainBoard.html', \
								user_id = user_id, \
								releaseTime = releaseTime, \
								hostname = hostname, \
								port = port, \
								hostHealth = hostHealth, \
								serName_A = serialName_A, \
								ups_Life_A = ups_Life_A, \
								inputVolt_A = inputVolt_A, \
								inputFreq_A = inputFreq_A, \
								inputLine_A = inputLine_A, \
								systemMode_A = str(systemMode_A), \
								outputLine_A = outputLine_A, \
								outputVolt_A = outputVolt_A, \
								outputAmp_A = Decimal(outputAmp_A)*1, \
								outputPercent_A = outputPercent_A, \
								outputWatt_A = outputWatt_A, \
								outputFreq_A = outputFreq_A, \
								batteryHealth_A = batteryHealth_A, \
								batteryStatus_A = batteryStatus_A, \
								batteryCharge_Mode_A = batteryCharge_Mode_A, \
								batteryRemain_Min_A = batteryRemain_Min_A, \
								batteryRemain_Sec_A = batteryRemain_Sec_A, \
								batteryVolt_A = batteryVolt_A, \
								batteryTemp_A = batteryTemp_A, \
								batteryRemain_Percent_A = batteryRemain_Percent_A, \
								lastBattery_Year_A = lastBattery_Year_A, \
								lastBattery_Mon_A = lastBattery_Mon_A, \
								lastBattery_Day_A = lastBattery_Day_A, \
								nextBattery_Year_A = nextBattery_Year_A, \
								nextBattery_Mon_A = nextBattery_Mon_A, \
								nextBattery_Day_A = nextBattery_Day_A, \
								serName_B = serialName_B, \
								ups_Life_B = ups_Life_B, \
								inputVolt_B = inputVolt_B, \
								inputFreq_B = inputFreq_B, \
								inputLine_B = inputLine_B, \
								systemMode_B = str(systemMode_B), \
								outputLine_B = outputLine_B, \
								outputVolt_B = outputVolt_B, \
								outputAmp_B = Decimal(outputAmp_B)*1, \
								outputPercent_B = outputPercent_B, \
								outputWatt_B = outputWatt_B, \
								outputFreq_B = outputFreq_B, \
								batteryHealth_B = batteryHealth_B, \
								batteryStatus_B = batteryStatus_B, \
								batteryCharge_Mode_B = batteryCharge_Mode_B, \
								batteryRemain_Min_B = batteryRemain_Min_B, \
								batteryRemain_Sec_B = batteryRemain_Sec_B, \
								batteryVolt_B = batteryVolt_B, \
								batteryTemp_B = batteryTemp_B, \
								batteryRemain_Percent_B = batteryRemain_Percent_B, \
								lastBattery_Year_B = lastBattery_Year_B, \
								lastBattery_Mon_B = lastBattery_Mon_B, \
								lastBattery_Day_B = lastBattery_Day_B, \
								nextBattery_Year_B = nextBattery_Year_B, \
								nextBattery_Mon_B = nextBattery_Mon_B, \
								nextBattery_Day_B = nextBattery_Day_B, \
								)
				else:
					print('USER NOT LOGIN !')
					print('-------------------------------')
					return redirect('/login')
			if x == len(memberList) - 1:
				print('USER NOT ON Member List !')
				print('-------------------------------')
				return redirect('/login')
	else:
		conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
		cursor = conn.cursor()
		temp = "UPDATE member SET mIP = '0.0.0.0' WHERE mId = '" + user_id + "'"
	#	print(temp)
		cursor.execute(temp)
		conn.commit()
		cursor.close()
		return redirect('/login')
@app.route('/history/<user_id>', methods=['POST', 'GET'])
def history(user_id):
	if request.method == 'GET':
		return '這是歷史頁面-%s' % user_id
	else:
		pass

@app.route('/login/', methods=['GET', 'POST'])
def login():
	print('-------------------------------')
	print("Login Client IP : " + request.remote_addr)
	if request.method == 'GET':
		return render_template('login.html')
	else:
		errorCode_A = errorCode_B = 0
		error = ''
		print(request.form)
		user_id = request.form.get('user_id')
		if user_id == None:
			errorCode_A = 1
		else:
			for x in list(user_id):
				if x == ' ':
					errorCode_A = 1
		if user_id != None and user_id != '' and errorCode_A != 1 and len(user_id) <= 10 and len(user_id) >= 4:
			conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
			cursor = conn.cursor()
			cursor.execute("SELECT mId FROM member")
			memberList = cursor.fetchall()
			conn.close()
			tmp = ''
		#	print(memberList)
			for x in range(0, len(memberList)):
				tmp = ''
				for y in list(str(memberList[x]).split("'")[1]):
					if y != ' ':
					#	print('/' + y + '/')
						tmp = tmp + y
					else:
						break
				if tmp == user_id:
					print(user_id)
					user_pwd = request.form.get('user_pwd')
					for x in list(user_pwd):
						if x == ' ':
							errorCode_A = 1
							break
					if user_pwd != '' and errorCode != 1:
						conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
						cursor = conn.cursor()
						temp = "SELECT mPassword FROM member WHERE mId = '" + tmp + "'"
					#	print(temp)
						cursor.execute(temp)
						checkPassword = cursor.fetchall()
					#	print(checkPassword)
						cursor.close()
						checkMember = 0
						password = ''
						for z in list(str(checkPassword[0]).split("'")[1]):
							if z != ' ':
							#	print('/' + z + '/')
								password = password + z
							else:
								break
						if user_pwd == password:
							conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
							cursor = conn.cursor()
							temp = "UPDATE member SET mIP = '" + request.remote_addr + "' WHERE mId = '" + user_id + "'"
							print(temp)
							cursor.execute(temp)
							conn.commit()
							cursor.close()
							login_ok = url_for('index', user_id = user_id)
							return redirect(login_ok)
						else:
							print('user_pwd Error !')
							errorCode_A = 1
					else:
						print('user_pwd Error !')
						errorCode_A = 1
				if x == len(memberList) - 1 and errorCode_A != 1:
					print('user_id Error !')
					errorCode_A = 1
		else:
			print('user_block input Error !')
			errorCode_A = 1
		print("errorCode_A = " + str(errorCode_A))
		ups_id = request.form.get('ups_id')
		if ups_id == None:
			errorCode_B = 1
		else:
			for x in list(ups_id):
				if x == ' ':
					errorCode_B = 1
		if ups_id != None and ups_id != '' and errorCode_B != 1 and len(ups_id) <= 10 and len(ups_id) >= 4:
			print('Key in ups_id = ' + ups_id)
			conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
			cursor = conn.cursor()
			temp = "SELECT uId FROM ups"
		#	print(temp)
			cursor.execute(temp)
			upsList = cursor.fetchall()
			conn.close()
			for x in range(0, len(upsList)):
			#	print(str(upsList[x]))
				tmp = ''
				for y in list(str(upsList[x]).split("'")[1]):
					if y != ' ':
					#	print('/' + y + '/')
						tmp = tmp + y
					else:
						break
				if tmp == ups_id:	
				#	print(tmp)
					conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
					cursor = conn.cursor()
					cursor.execute("SELECT mId FROM ups WHERE uId = '" + ups_id + "'")
					memberList = cursor.fetchall()
					conn.close()
					tmp = ''
					for y in list(str(memberList[0]).split("'")[1]):
						if y != ' ':
						#	print('/' + y + '/')
							tmp = tmp + y
						else:
							break
					ups_pwd = request.form.get('ups_pwd')
					for x in list(ups_pwd):
						if x == ' ':
							errorCode_B = 1
							break
					if ups_pwd != '' and errorCode_B != 1:
						conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
						cursor = conn.cursor()
						temp = "SELECT mPassword FROM member WHERE mId = '" + tmp + "'"
					#	print(temp)
						cursor.execute(temp)
						checkPassword = cursor.fetchall()
					#	print(checkPassword)
						cursor.close()
						checkMember = 0
						password = ''
						for z in list(str(checkPassword[0]).split("'")[1]):
							if z != ' ':
							#	print('/' + z + '/')
								password = password + z
							else:
								break
					#	print(password)
						if ups_pwd == password:
							print('-------------------------------')
							conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
							cursor = conn.cursor()
							temp = "UPDATE member SET mIP = '" + request.remote_addr + "' WHERE mId = '" + tmp + "'"
							print(temp)
							cursor.execute(temp)
							conn.commit()
							cursor.close()
							login_ok = url_for('index', user_id = tmp)
							return redirect(login_ok)
						else:
							errorCode_B = 1
				if x == len(upsList) - 1 and errorCode_B != 1:
					print('ups_id Error !')
					errorCode_B = 1
		else:
			print('ups_block input Error !')
			errorCode_B = 1
		print("errorCode_B = " + str(errorCode_B))
		if errorCode_A == 1 or errorCode_B == 1:
			print('user / ups Error !')
			print('-------------------------------')
			error = '請確認輸入的資料 !'
			return render_template('login.html', error = error)

@app.route('/user_signup', methods=['GET', 'POST'])
def user_signup():
	print('-------------------------------')
	print("User Regist Client IP : " + request.remote_addr)
	errorCode = 0
	if request.method == 'GET':	
		print('-------------------------------')
		error = ''
		return render_template('userSignup.html', error = error)
	else:
		print('-------------------------------')
	#	print (request.form)
		user_id = request.form.get('user_id')
		for x in list(user_id):
			if x == ' ':
				errorCode = 1
		if user_id != '' and errorCode == 0 and len(user_id) <= 10 and len(user_id) >= 4:
			print("user_id : " + user_id)
			user_pwd = request.form.get('user_pwd')
			countLower = countUpper = countNumber = 0
			for x in list(user_pwd):
				if x == ' ':
					errorCode = 1
				elif ord(x) >= 97 and ord(x) <= 122:
					countLower = countLower + 1
				elif ord(x) >= 65 and ord(x) <= 90:
					countUpper = countUpper + 1
				elif ord(x) >= 48 and ord(x) <= 57:
					countNumber = countNumber + 1
			if user_pwd != '' and len(user_pwd) > 8 and len(user_pwd) <= 30 and countLower > 0 or countUpper > 0 or countNumber > 0 and errorCode == 0:
				print("user_pwd : " + user_pwd)
				user_name = request.form.get('user_name')
				for x in list(user_name):
					if x == ' ':
						errorCode = 1
				if user_name != '' and errorCode == 0 and len(user_name) > 4 and len(user_name) <= 30:
					print("user_name : " + user_name)
					user_phone = request.form.get('user_phone')
					tmp = user_phone.split('-')
					if user_phone != '' and len(user_phone) == 12 and int(tmp[0]) <= 999 and int(tmp[1]) <= 999 and int(tmp[2]) <= 999:
						user_mail = request.form.get('user_mail')
						tmp = user_mail.split('@')
						if user_phone != '' and tmp[0] != '' and tmp[1] != '':	
							user_rule = request.form.get('user_rule')
							if user_rule != None:
								user_collect = request.form.get('user_collect')
								if user_collect != None:
									user_collect=1
								else:
									user_collect=0
								print("user_collect : " + str(user_collect))
								conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
								cursor = conn.cursor()
								cursor.execute('SELECT mId FROM member')
								memberList = cursor.fetchall()
								cursor.close()
								for x in range(0, len(memberList)):
								#	print(str(memberList[x]))
									tmp = ''
									for y in list(str(memberList[x]).split("'")[1]):
										if y != ' ':
										#	print('/' + y + '/')
											tmp = tmp + y
										else:
											break
									if tmp == user_id:
										errorCode = 1
								#	print(tmp)
								if errorCode == 0:
									cursor = conn.cursor()
									addMember = "INSERT INTO dbo.member (mId, mPassword, mName, mEmail, mPhone, mCollect) VALUES ('" + user_id + "' , '" + user_pwd + "', '" + user_name + "', '" +  user_mail + "', '" + user_phone + "', " + str(user_collect) +")"
								#	print(addMember)
									cursor.execute(addMember)
									conn.commit()
									conn.close()
									print("DB Incert : OK !")
									print('-------------------------------')
									login_check = url_for('login')
									return redirect(login_check)
								else:
									print("DB Incert : NO !")
									print('-------------------------------')
									error = '此帳號ID被使用，請進行更改'
									return render_template('userSignup.html', error = error)
							else:
								print('user_acess Error !')
								print('-------------------------------')
								error = '請確認已閱讀管理者條文'
								return render_template('userSignup.html', error = error)
						else:
							print('user_mail Error !')
							print('-------------------------------')
							error = '請確認輸入的電子郵件'
							return render_template('userSignup.html', error = error)
					else:
						print('user_phone Error !')
						print('-------------------------------')
						error = '請確認輸入的電話號碼'
						return render_template('userSignup.html', error = error)
				else:
					print('user_name Error !')
					print('-------------------------------')
					error = '請確認輸入的姓名'
					return render_template('userSignup.html', error = error)	
			else:
				print('user_pwd Error !')
				print('-------------------------------')
				error = '請確認輸入的密碼'
				return render_template('userSignup.html', error = error)	
		else:
			print('user_id Error !')
			print('-------------------------------')
			error = '請確認輸入的帳號'
			return render_template('userSignup.html', error = error)

@app.route('/ups_signup/<user_id>', methods=['GET', 'POST'])
def ups_signup(user_id):
	print('-------------------------------')
	print("UPS Regist Client IP : " + request.remote_addr)
	errorCode = 0
	if request.method == 'GET':	
		print('-------------------------------')
		error = ''
		conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
		cursor = conn.cursor()
		temp = "SELECT mId FROM member"
	#	print(temp)
		cursor.execute(temp)
		memberList = cursor.fetchall()
		conn.commit()
		cursor.close()
		tmp = ''
		for x in range(0, len(memberList)):
			tmp = ''
			for y in list(str(memberList[x]).split("'")[1]):
				if y != ' ':
				#	print('/' + y + '/')
					tmp = tmp + y
				else:
					break
			if tmp == user_id:
				conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
				cursor = conn.cursor()
				temp = "SELECT mIP FROM member WHERE mId = '" + user_id + "'"
			#	print(temp)
				cursor.execute(temp)
				ipList = cursor.fetchall()
				conn.commit()
				cursor.close()
				tmp = ''
				for z in list(str(ipList[0]).split("'")[1]):
					if z != ' ':
					#	print('/' + z + '/')
						tmp = tmp + z
					else:
						break
				if tmp == request.remote_addr:		
					print('Login IP :' + tmp)
					return render_template('upsSignup.html', user_id = user_id)
				else:
					print('USER NOT ON Member List !')
					print('-------------------------------')
					return redirect('/login')
			if x == len(memberList) - 1:
				print('USER NOT LOGIN !')
				print('-------------------------------')
				return redirect('/login')
	else:
		print('-------------------------------')
		print (request.form)
		ups_id = request.form.get('ups_id')
		for x in list(ups_id):
			if x == ' ':
				errorCode = 1
		if ups_id != '' and errorCode == 0 and len(ups_id) <= 10 and len(ups_id) >= 4:
			print("ups_id : " + ups_id)
			conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
			cursor = conn.cursor()
			cursor.execute('SELECT uId FROM ups')
			upsList = cursor.fetchall()
			cursor.close()
			for x in range(0, len(upsList)):
			#	print(str(upsList[x]))
				tmp = ''
				for y in list(str(upsList[x]).split("'")[1]):
					if y != ' ':
					#	print('/' + y + '/')
						tmp = tmp + y
					else:
						break
				if tmp == ups_id:
					errorCode = 1
			#	print(tmp)
			if errorCode != 1:
				print("user_id : " + user_id)
				conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
				cursor = conn.cursor()
				cursor.execute('SELECT mId FROM member')
				memberList = cursor.fetchall()
				cursor.close()
				checkMember = 0
				for x in range(0, len(memberList)):
				#	print(str(memberList[x]))
					tmp = ''
					for y in list(str(memberList[x]).split("'")[1]):
						if y != ' ':
						#	print('/' + y + '/')
							tmp = tmp + y
						else:
							break
					if tmp == user_id:
						user_pwd = request.form.get('user_pwd')
						for x in list(user_pwd):
							if x == ' ':
								errorCode = 1
								break
						if user_pwd != '' and errorCode != 1:
							conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
							cursor = conn.cursor()
							temp = "SELECT mPassword FROM member WHERE mId = '" + tmp + "'"
						#	print(temp)
							cursor.execute(temp)
							checkPassword = cursor.fetchall()
							print(checkPassword)
							cursor.close()
							password = ''
							for z in list(str(checkPassword[0]).split("'")[1]):
								if z != ' ':
								#	print('/' + z + '/')
									password = password + z
								else:
									break
							if user_pwd == password:
								print("password : PASS !")
								ups_name = request.form.get('ups_name')
								for x in list(ups_name):
									if x == ' ':
										errorCode = 1
										break
								if ups_name != '' and errorCode != 1:
									ups_ip = request.form.get('ups_ip')
									try:
										ip = ups_ip.split(":")[0].split('.')
										port = int(ups_ip.split(":")[1])
									except:
										errorCode = 1
								#	print("IP : " + ip[0] + "." + ip[1] + "." + ip[2] + "." + ip[3])
								#	print("PORT : " + str(port))
									if ups_ip != '' and errorCode!= 1 and len(ip) == 4 and int(ip[0]) <= 254 and int(ip[1]) <= 254 and int(ip[2]) <= 254 and int(ip[3]) <= 254 and port <= 30080:
										print("ups_ip : " + ups_ip)
										ups_create = request.form.get('ups_create')
										if (ups_create != 'None'):
											ups_model = request.form.get('ups_model')
											print('ups_model : ' + ups_model)
											if (ups_model != 'None'):
												ups_unit = request.form.get('ups_unit')
												print('ups_unit : ' + ups_unit)
												ups_number = request.form.get('ups_number')
												if (ups_number != ''):
													print('ups_number : ' + ups_number)
													ups_locate = request.form.get('ups_locate')
													if (ups_locate != ''):
														print('ups_locate : ' + ups_locate)
														ups_rule = request.form.get('ups_rule')
														if ups_rule != None:
															ups_collect = request.form.get('ups_collect')
															if ups_collect != None:
																ups_collect=1
															else:
																ups_collect=0
															print("ups_collect : " + str(ups_collect))
															cursor = conn.cursor()
															addUPS = "INSERT INTO dbo.ups (uId, mId, uName, uIP, uFactory, uModel, uUnit, uNumber, uDistance, uCollect) VALUES ('" + ups_id + "' , '" + user_id + "', '" + ups_name + "', '" + ups_ip + "', '" +  ups_create + "', '" + ups_model + "', '" + ups_unit + "', '" + ups_number + "', '" + ups_locate +  "', " + str(ups_collect) + ")"
														#	print(addUPS)
															cursor.execute(addUPS)
															conn.commit()
															conn.close()
															print("DB Incert : OK !")
															print('-------------------------------')
															error = '設備添加成功 !'
															return render_template('upsSignup.html', error = error, user_id = user_id)
														else:
															print('ups_acess Error !')
															print('-------------------------------')
															error = '請確認已閱讀UPS設備託管條文'
															return render_template('upsSignup.html', error = error, user_id = user_id)
													else:
														print('ups_locate Error !')
														print('-------------------------------')
														error = '請填寫設備的放置區域或備註信息'
														return render_template('upsSignup.html', error = error, user_id = user_id)
												else:
													print('ups_number Error !')
													print('-------------------------------')
													error = '請確認設備的識別編號'
													return render_template('upsSignup.html', error = error, user_id = user_id)	
											else:
												print('ups_model Error !')
												print('-------------------------------')
												error = '請確認設備的所屬系列'
											return render_template('upsSignup.html', error = error, user_id = user_id)	
										else:
											print('ups_create Error !')
											print('-------------------------------')
											error = '請確認設備的生產廠區'
											return render_template('upsSignup.html', error = error, user_id = user_id)	
									else:
										print('ups_ip Error !')
										print('-------------------------------')
										error = '請確認設備的託管 IP'
										return render_template('upsSignup.html', error = error, user_id = user_id)	
								else:
									print('ups_name Error !')
									print('-------------------------------')
									error = '請確認輸入的託管 設備名稱'
									return render_template('upsSignup.html', error = error, user_id = user_id)
							else:
								errorCode = 1
								print('ups_pwd Error !')
								print('-------------------------------')
								error = '請確認輸入的管理者資料'
								return render_template('upsSignup.html', error = error, user_id = user_id)
						else:
							errorCode = 1
							print('ups_pwd Error !')
							print('-------------------------------')
							error = '請確認輸入的管理者資料'
							return render_template('upsSignup.html', error = error, user_id = user_id)
					if x == len(memberList) - 1 and errorCode != 1:
						print('ups_id Error !')
						print('-------------------------------')
						error = '請確認輸入的管理者資料'
						return render_template('upsSignup.html', error = error, user_id = user_id)
			else:
				print('user_id Error !')
				print('-------------------------------')
				error = 'UPS 編號已被使用'
				return render_template('upsSignup.html', error = error, user_id = user_id)			
		else:
			print('user_id Error !')
			print('-------------------------------')
			error = '請確認輸入的 UPS 編號'
			return render_template('upsSignup.html', error = error, user_id = user_id)

@app.route('/user_replace/<user_id>', methods=['GET', 'POST'])
def user_replace(user_id):
	print('-------------------------------')
	print("USER Replace Client IP : " + request.remote_addr)
	errorCode = 0
	if request.method == 'GET':	
		print('-------------------------------')
		error = ''
		conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
		cursor = conn.cursor()
		temp = "SELECT mId FROM member"
	#	print(temp)
		cursor.execute(temp)
		memberList = cursor.fetchall()
		conn.commit()
		cursor.close()
		tmp = ''
		for x in range(0, len(memberList)):
			tmp = ''
			for y in list(str(memberList[x]).split("'")[1]):
				if y != ' ':
				#	print('/' + y + '/')
					tmp = tmp + y
				else:
					break
			if tmp == user_id:
				conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
				cursor = conn.cursor()
				temp = "SELECT mIP FROM member WHERE mId = '" + user_id + "'"
			#	print(temp)
				cursor.execute(temp)
				ipList = cursor.fetchall()
				conn.commit()
				cursor.close()
				tmp = ''
				for z in list(str(ipList[0]).split("'")[1]):
					if z != ' ':
					#	print('/' + z + '/')
						tmp = tmp + z
					else:
						break
				if tmp == request.remote_addr:		
					print('Login IP :' + tmp)
					return render_template('userReplace.html', error = error, user_id = user_id)
				else:
					print('USER NOT LOGIN !')
					print('-------------------------------')
					return redirect('/login')
			if x == len(memberList) - 1:
				print('USER NOT ON Member List !')
				print('-------------------------------')
				return redirect('/login')

	else:
		print('-------------------------------')
	#	print (request.form)
		print("user_id : " + user_id)
		print('-------------------------------')
		conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
		cursor = conn.cursor()
		cursor.execute("SELECT mId FROM member")
		memberList = cursor.fetchall()
		conn.close()
		error = "已更改 : "
		for x in range(0, len(memberList)-1):
			tmp = ''
			for y in list(str(memberList[x]).split("'")[1]):
				if y != ' ':
				#	print('/' + y + '/')
					tmp = tmp + y
				else:
					break
		#	print("tmp : " + tmp)
			if tmp == user_id:
				user_pwd = request.form.get('user_pwd')
				for x in list(user_pwd):
					if x == ' ':
						errorCode = 1
						break
				if user_pwd != '' and errorCode != 1:
					conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
					cursor = conn.cursor()
					temp = "SELECT mPassword FROM member WHERE mId = '" + user_id + "'"
				#	print(temp)
					cursor.execute(temp)
					checkPassword = cursor.fetchall()
				#	print(checkPassword)
					cursor.close()
					checkMember = 0
					password = ''
					for z in list(str(checkPassword[0]).split("'")[1]):
						if z != ' ':
						#	print('/' + z + '/')
							password = password + z
						else:
							break
				#	print(password)
					if user_pwd == password:
						user_new_pwd_A = request.form.get('user_new_pwd_A')
						user_new_pwd_B = request.form.get('user_new_pwd_B')
						for x in list(user_new_pwd_A):
							if x == ' ':
								errorCode = 1
								break
						for x in list(user_new_pwd_B):
							if x == ' ':
								errorCode = 1
								break
						if user_new_pwd_A == user_new_pwd_B and user_new_pwd_A != '' and user_new_pwd_B != '' and errorCode != 1 and len(user_new_pwd_A) >= 8:
							conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
							cursor = conn.cursor()
							temp = "UPDATE member SET mPassword = '" + user_new_pwd_A + "' WHERE mId = '" + user_id + "'"
						#	print(temp)
							cursor.execute(temp)
							conn.commit()
							conn.close()
							error = error + "密碼 / "
						elif user_new_pwd_A == '' and user_new_pwd_B == '':
							print('user_password Not Change !')
							print('-------------------------------')
						else:
							print('user_password check Error !')
							print('-------------------------------')
							error = " 請驗證更新輸入的密碼"
							return render_template('userReplace.html', error = error, user_id = user_id)
						user_name = request.form.get('user_name')
						for x in list(user_name):
							if x == ' ':
								errorCode = 1
								break
						if user_name != '' and errorCode != 1:
							print("user_name : " + user_name)
							conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
							cursor = conn.cursor()
						#	temp = "UPDATE member SET mName = '" + user_name + "' WHERE mId = '" + user_id + "'"
							print(temp)
							cursor.execute(temp)
							conn.commit()
							cursor.close()
							error = error + "姓名 / "
						else:
							print('user_name Not Change !')
							print('-------------------------------')
						user_phone = request.form.get('user_phone')
						for x in list(user_phone):
							if x == ' ':
								errorCode = 1
								break
						if user_phone != '' and errorCode != 1:
							try:
								tmp = user_phone.split("-")
							except:
								errorCode = 1
							if errorCode != 1 and int(tmp[0]) <= 999 and int(tmp[1]) <= 999 and int(tmp[2]) <= 999:
								print("user_phone : " + user_phone)
								conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
								cursor = conn.cursor()
								temp = "UPDATE member SET mPhone = '" + user_phone + "' WHERE mId = '" + user_id + "'"
								print(temp)
								cursor.execute(temp)
								conn.commit()
								cursor.close()
								error = error + "電話 / "
							else:
								print('user_phone check Error !')
								print('-------------------------------')
								error = error + " 請驗證更新輸入的電話號碼"
								return render_template('userReplace.html', error = error, user_id = user_id)
						else:
							print('user_phone Not Change !')
							print('-------------------------------')
						
						user_mail = request.form.get('user_mail')
						for x in list(user_mail):
							if x == ' ':
								errorCode = 1
								break
						if user_mail != '' and errorCode != 1:
							try:
								tmp = user_mail.split('@')
							except:
								errorCode = 1
							if errorCode != 1 and tmp[0] != '' and tmp[1] != '':
								conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
								cursor = conn.cursor()
								temp = "UPDATE member SET mEmail = '" + user_mail + "' WHERE mId = '" + user_id + "'"
							#	print(temp)
								cursor.execute(temp)
								conn.commit()
								cursor.close()
								error = error + "電子信箱 / "
							else:
								print('user_mail check Error !')
								print('-------------------------------')
								error = error + " 請驗證更新輸入的電子信箱"
								return render_template('userReplace.html', error = error, user_id = user_id)
						else:
							print('user_mail Not Change !')
							print('-------------------------------')
						user_collect = request.form.get('user_collect')
						if user_collect != None:
							user_collect=1
							error = error + "參與資料收集 / "
						else:
							user_collect=0
							error = error + "取消資料收集 / "
						print("user_collect : " + str(user_collect))
						conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
						cursor = conn.cursor()
						temp = "UPDATE member SET mCollect = '" + str(user_collect) + "' WHERE mId = '" + user_id + "'"
					#	print(temp)
						cursor.execute(temp)
						conn.commit()
						cursor.close()
						print('-------------------------------')
						print('驗證成功')
						print('-------------------------------')
						error = error + '驗證成功'
						return render_template('userReplace.html', error = error, user_id = user_id)	
					else:
						errorCode = 1
				else:
					errorCode = 1		
			if x == len(memberList) - 1:
				errorCode = 1	
		if (errorCode == 1):
			print('user_Data Error !')
			print('-------------------------------')
			error = '請確認輸入的設備資料'
			return render_template('userReplace.html', error = error, user_id = user_id)

def find_ups(user_id):
	conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
	cursor = conn.cursor()
	cursor.execute("SELECT uId FROM ups WHERE mId = '" + user_id + "'")
	upsList = cursor.fetchall()
	cursor.close()
	return upsList

@app.route('/ups_replace/<user_id>', methods=['GET', 'POST'])
def ups_replace(user_id):
	print('-------------------------------')
	print("UPS Replace Client IP : " + request.remote_addr)
	errorCode = 0
	if request.method == 'GET':	
		print('-------------------------------')
		error = ''
		conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
		cursor = conn.cursor()
		temp = "SELECT mId FROM member"
		cursor.execute(temp)
		memberList = cursor.fetchall()
		print(memberList)
		conn.commit()
		cursor.close()
		tmp = ''
		for x in range(0, len(memberList)):
			tmp = ''
			for y in list(str(memberList[x]).split("'")[1]):
				if y != ' ':
				#	print('/' + y + '/')
					tmp = tmp + y
				else:
					break
			print(tmp)
			if tmp == user_id:
				conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
				cursor = conn.cursor()
				temp = "SELECT mIP FROM member WHERE mId = '" + user_id + "'"
			#	print(temp)
				cursor.execute(temp)
				ipList = cursor.fetchall()
				conn.commit()
				cursor.close()
				tmp = ''
				for z in list(str(ipList[0]).split("'")[1]):
					if z != ' ':
					#	print('/' + z + '/')
						tmp = tmp + z
					else:
						break
				if tmp == request.remote_addr:			
					print('Login IP :' + tmp)
					return render_template('upsReplace.html', msg = find_ups(user_id), user_id = user_id)
				else:
					print('USER NOT LOGIN !')
					print('-------------------------------')
					return redirect('/login')
			if x == len(memberList) - 1:
				print('USER NOT ON Member List !')
				print('-------------------------------')
				return redirect('/login')
	else:
		print('-------------------------------')
	#	print (request.form)
		error = "已更改 : "
		ups_id = request.form.get('ups_id')
		for x in list(ups_id):
			if x == ' ':
				errorCode = 1
				break
		if ups_id != '' and errorCode == 0 and len(ups_id) <= 10 and len(ups_id) >= 4:
			print("ups_id : " + ups_id)
			print('-------------------------------')
			conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
			cursor = conn.cursor()
			cursor.execute('SELECT uId FROM ups')
			upsList = cursor.fetchall()
			cursor.close()
			for x in range(0, len(upsList)):
			#	print(str(upsList[x]))
				tmp = ''
				for y in list(str(upsList[x]).split("'")[1]):
					if y != ' ':
					#	print('/' + y + '/')
						tmp = tmp + y
					else:
						break
				if tmp == ups_id:	
				#	print(tmp)
					print("user_id : " + user_id)
					conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
					cursor = conn.cursor()
					cursor.execute("SELECT mId FROM ups WHERE uId = '" + ups_id + "'")
					memberList = cursor.fetchall()
					conn.close()
					tmp = ''
					for y in list(str(memberList[0]).split("'")[1]):
						if y != ' ':
						#	print('/' + y + '/')
							tmp = tmp + y
						else:
							break
					if tmp == user_id:
						user_pwd = request.form.get('user_pwd')
						for x in list(user_pwd):
							if x == ' ':
								errorCode = 1
								break
						if user_pwd != '' and errorCode != 1:
							conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
							cursor = conn.cursor()
							temp = "SELECT mPassword FROM member WHERE mId = '" + tmp + "'"
						#	print(temp)
							cursor.execute(temp)
							checkPassword = cursor.fetchall()
						#	print(checkPassword)
							cursor.close()
							checkMember = 0
							password = ''
							for z in list(str(checkPassword[0]).split("'")[1]):
								if z != ' ':
								#	print('/' + z + '/')
									password = password + z
								else:
									break
						#	print(password)
							if user_pwd == password:
								print('-------------------------------')
								ups_name = request.form.get('ups_name')
								for x in list(ups_name):
									if x == ' ':
										errorCode = 1
										break
								if ups_name != '' and errorCode != 1:
									conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
									cursor = conn.cursor()
									temp = "UPDATE ups SET uName = '" + ups_name + "' WHERE uId = '" + ups_id +"' AND mId = '" + user_id + "'"
								#	print(temp)
									cursor.execute(temp)
									conn.commit()
									cursor.close()
									error = error + "設備名稱 / "
								else:
									print('ups_name Not Change !')
									print('-------------------------------')
								ups_ip = request.form.get('ups_ip')
								for x in list(ups_ip):
									if x == ' ':
										errorCode = 1
										break
								if ups_ip != '' and errorCode != 1:
									try:
										ip = ups_ip.split(":")[0].split('.')
										port = int(ups_ip.split(":")[1])
									except:
										errorCode = 1
								#	print("IP : " + ip[0] + "." + ip[1] + "." + ip[2] + "." + ip[3])
								#	print("PORT : " + str(port))
									if ups_ip != '' and errorCode != 1 and len(ip) == 4 and int(ip[0]) <= 254 and int(ip[1]) <= 254 and int(ip[2]) <= 254 and int(ip[3]) <= 254 and port <= 30080:
										print("ups_ip : " + ups_ip)
										conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
										cursor = conn.cursor()
										temp = "UPDATE ups SET uIP = '" + ups_ip + "' WHERE uId = '" + ups_id +"' AND mId = '" + user_id + "'"
										print(temp)
										cursor.execute(temp)
										conn.commit()
										conn.close()
										error = error + "託管IP / "
									else:
										print('ups_ip Error !')
										print('-------------------------------')
										error = error + '請確認輸入的託管 IP'
										return render_template('upsReplace.html', error = error, msg = find_ups(user_id), user_id = user_id)
								else:
									print('ups_ip Not Change !')
									print('-------------------------------')
								ups_create = request.form.get('ups_create')
								if ups_create != 'None':
									print("ups_creat : " + ups_create)
									conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
									cursor = conn.cursor()
									temp = "UPDATE ups SET uFactory = '" + ups_create + "' WHERE uId = '" + ups_id +"' AND mId = '" + user_id + "'"
									print(temp)
									cursor.execute(temp)
									conn.commit()
									cursor.close()
									error = error + "生產廠區 / "
								else:
									print('ups_create Not Change !')
									print('-------------------------------')
								ups_model = request.form.get('ups_model')
								if ups_model != 'None':
									print("ups_model : " + ups_model)
									ups_unit = request.form.get('ups_unit')
									conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
									cursor = conn.cursor()
									temp = "UPDATE ups SET uModel = '" + ups_model + "', uUnit = '" + ups_unit + "' WHERE uId = '" + ups_id +"' AND mId = '" + user_id + "'"
									print(temp)
									cursor.execute(temp)
									conn.commit()
									cursor.close()
									error = error + "設備系列&容量 / "
								else:
									print('ups_model Not Change !')
									print('-------------------------------')
								ups_locate = request.form.get('ups_locate')
								for x in list(ups_locate):
									if x == ' ':
										errorCode = 1
										break
								if ups_locate != '' and errorCode != 1:
									conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
									cursor = conn.cursor()
									temp = "UPDATE ups SET uDistance = '" + ups_locate + "' WHERE uId = '" + ups_id +"' AND mId = '" + user_id + "'"
								#	print(temp)
									cursor.execute(temp)
									conn.commit()
									cursor.close()
									error = error + "設備地點 / "
								else:
									print('ups_locate Not Change !')
									print('-------------------------------')
								ups_collect = request.form.get('ups_collect')
								if ups_collect != None:
									ups_collect=1
									error = error + "參與資料收集 / "
								else:
									ups_collect=0
									error = error + "取消資料收集 / "
								print("ups_collect : " + str(ups_collect))
								print('-------------------------------')
								conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
								cursor = conn.cursor()
								temp = "UPDATE ups SET uCollect = '" + str(ups_collect) + "' WHERE uId = '" + ups_id +"' AND mId = '" + user_id + "'"
							#	print(temp)
								cursor.execute(temp)
								conn.commit()
								cursor.close()
								print('驗證成功')
								print('-------------------------------')
								error = error + '驗證成功'
								return render_template('upsReplace.html', msg = find_ups(user_id), error = error, user_id = user_id)	
						else:
							errorCode = 1
					else:
						errorCode = 1
				if x == len(upsList) - 1:
					errorCode = 1		
		else:
			errorCode = 1				
		if (errorCode == 1):
			print('ups_id Error !')
			print('-------------------------------')
			error = '請確認輸入的設備資料'
			conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
			cursor = conn.cursor()
			temp = "SELECT uId FROM ups WHERE mId = '" + user_id + "'"
		#	print(temp)
			cursor.execute(temp)
			upsList = cursor.fetchall()
		#	print(upsList)
			cursor.close()
			return render_template('upsReplace.html', msg = find_ups(user_id), error = error, user_id = user_id)			

@app.route('/ups_delete/<user_id>', methods=['GET', 'POST'])
def ups_delete(user_id):
	print('-------------------------------')
	print("UPS Delete Client IP : " + request.remote_addr)
	errorCode = 0
	if request.method == 'GET':	
		print('-------------------------------')
		error = ''
		conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
		cursor = conn.cursor()
		temp = "SELECT mId FROM member"
		cursor.execute(temp)
		memberList = cursor.fetchall()
		print(memberList)
		conn.commit()
		cursor.close()
		tmp = ''
		for x in range(0, len(memberList)):
			tmp = ''
			for y in list(str(memberList[x]).split("'")[1]):
				if y != ' ':
				#	print('/' + y + '/')
					tmp = tmp + y
				else:
					break
			print(tmp)
			if tmp == user_id:
				conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
				cursor = conn.cursor()
				temp = "SELECT mIP FROM member WHERE mId = '" + user_id + "'"
			#	print(temp)
				cursor.execute(temp)
				ipList = cursor.fetchall()
				conn.commit()
				cursor.close()
				tmp = ''
				for z in list(str(ipList[0]).split("'")[1]):
					if z != ' ':
					#	print('/' + z + '/')
						tmp = tmp + z
					else:
						break
				if tmp == request.remote_addr:			
					print('Login IP :' + tmp)
					conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
					cursor = conn.cursor()
					temp = "SELECT uId FROM ups WHERE mId = '" + user_id + "'"
				#	print(temp)
					cursor.execute(temp)
					upsList = cursor.fetchall()
					print(upsList)
					cursor.close()
					return render_template('upsDelete.html', msg = upsList, user_id = user_id)
				else:
					print('USER NOT ON Member List !')
					print('-------------------------------')
					return redirect('/login')
			if x == len(memberList) - 1:
				print('USER NOT LOGIN !')
				print('-------------------------------')
				return redirect('/login')
	else:
		print('-------------------------------')
	#	print (request.form)
		ups_id = request.form.get('ups_id')
		for x in list(ups_id):
			if x == ' ':
				errorCode = 1
			break
		if ups_id != '' and errorCode == 0 and len(ups_id) <= 10 and len(ups_id) >= 4:
			print("ups_id : " + ups_id)
			conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
			cursor = conn.cursor()
			cursor.execute('SELECT uId FROM ups')
			upsList = cursor.fetchall()
			cursor.close()
			for x in range(0, len(upsList)):
			#	print(str(upsList[x]))
				tmp = ''
				for y in list(str(upsList[x]).split("'")[1]):
					if y != ' ':
					#	print('/' + y + '/')
						tmp = tmp + y
					else:
						break
				if tmp == ups_id:	
					print("user_id : " + user_id)
					conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
					cursor = conn.cursor()
					cursor.execute("SELECT mId FROM ups WHERE uId = '" + ups_id + "'")
					memberList = cursor.fetchall()
					conn.close()
					tmp = ''
					for y in list(str(memberList[0]).split("'")[1]):
						if y != ' ':
						#	print('/' + y + '/')
							tmp = tmp + y
						else:
							break
					if tmp == user_id:
						user_pwd = request.form.get('user_pwd')
						for x in list(user_pwd):
							if x == ' ':
								errorCode = 1
								break
						if user_pwd != '' and errorCode != 1:
							conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
							cursor = conn.cursor()
							temp = "SELECT mPassword FROM member WHERE mId = '" + tmp + "'"
						#	print(temp)
							cursor.execute(temp)
							checkPassword = cursor.fetchall()
							print(checkPassword)
							cursor.close()
							checkMember = 0
							password = ''
							for z in list(str(checkPassword[0]).split("'")[1]):
								if z != ' ':
								#	print('/' + z + '/')
									password = password + z
								else:
									break
							if user_pwd == password:
								print("password : PASS !")
								conn = pymssql.connect(server="163.17.136.65", user="1410432021", password="H124906356a", database="1410432021")
								cursor = conn.cursor()
								temp = "UPDATE ups SET uDistance = '" + ups_locate + "' WHERE uId = '" + ups_id +"' AND mId = '" + user_id + "'"
							#	print(temp)
								cursor.execute(temp)
								conn.commit()
								cursor.close()
								redelete = url_for("upsDelete")
								return redirect(redelete)
						else:
							errorCode = 1
					else:
						errorCode = 1
				if x == len(upsList) - 1 and errorCode != 1:
						print('ups_id Error !')
						errorCode = 1
		else:
			errorCode = 1
		if errorCode == 1:
			print("Delete Data Error !")
			print('-------------------------------')
			error = "請確認輸入資料"
			return render_template('upsDelete.html', user_id = user_id, error = error, msg = find_ups(user_id))

if __name__ == '__main__':
#	app.run(debug = True)
	app.run(host = '0.0.0.0', port = 3000, debug = True)