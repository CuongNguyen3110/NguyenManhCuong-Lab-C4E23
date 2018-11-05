import datetime
from gmail import GMail, Message
from random import choice

now = datetime.datetime.now()

sickness_list = ["thương hàn", "kiết lị", "tiêu chảy"]

gmail = GMail("cuongnguyen1.fit@gmail.com", "footballistaste")
template = '''
    <p>Ch&agrave;o sếp,</p>
    <p>H&ocirc;m nay em ngủ dậy, thấy đau bụng, b&aacute;c sỹ bảo em bị Ebola.</p>
    <p>Sếp cho em nghỉ l&agrave;m nh&eacute;&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" />,</p>
    <p>Nh&acirc;n vi&ecirc;n của sếp&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-tongue-out.gif" alt="tongue-out" /></p>
    <p>&nbsp;</p>
    '''
sickness = choice(sickness_list)

symptom = "dau bung"
content = template.replace("{{sick}}", sickness).replace("{{symptom}}", symptom)
message =  Message("Xin nghi lam", to="cuongnm3110@gmail.com", html=content)

if now.hour == 7:
    gmail.send(message)

