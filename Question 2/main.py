import pygame
import os
import random
filepath = os.path.abspath(__file__)
filedir = os.path.dirname(filepath)
pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.mixer.music.load(filedir + str('\Music\Life Goes On - Persona 5.mp3'))
#Music reference: Meguro, S. (2017). Persona 5 Original Soundtrack: Life Goes On [CD]. Tokyo: Atlus.
game_status = 'start'
scriptLine = 0
questionLine = 0
name = ''
Feelings = ''
questionsList = []
TeacherMood = ''
generator = 0
rightAnswer = ''
rightAnswerNo= 0
ExamScore = 0
MaxExamScore = 0

while game_status == 'start':
        win = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Exam Simulator")
        x = 250
        y = 250
        width = 350
        height = 50
        vol = 5
        background_image = pygame.image.load(filedir + str('\\pics\\bg Outside.png'))
        #Taken from wikipedia: Charles Darwin University. (2020). Retrieved 18 October 2020, from https://en.wikipedia.org/wiki/Charles_Darwin_University
        win.blit(background_image, [0, 0])
        pygame.draw.rect(win,(255,255,255), (x, y, width, height))
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Exam Simulator', True, (0,0,0))
        win.blit(text,(250,260))
        pygame.display.update()
        for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = event.pos 
                    if 550 > mousex > 250  and 300 > mousey > 250:
                            pygame.mixer.music.play(-1)
                            game_status = 'intro'
        
while game_status == 'intro':
        win = pygame.display.set_mode((800,600))
        win.blit(background_image, [0, 0])
        script = open(filedir + '/script/' + game_status + '.txt', 'r')
        lines = script.readlines()
        if lines[questionLine].startswith('Question'):
                theQuestion = (lines[questionLine][13:].strip('\n'))
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render(str(theQuestion), True, (0,0,0))
                win.blit(text,(50,50))
                questions = lines[questionLine][10:].split()[0]
                game_status = 'chooseName'
                
        else:
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render(str(lines[scriptLine]).strip('\n'), True, (0,0,0))
                win.blit(text,(50,50))
                questionLine = scriptLine
        teacher = pygame.transform.scale(pygame.image.load(filedir + '\pics\P3_Edogawa_Render.png'), (350, 450))
        win.blit(teacher,(450,260))
        pygame.display.update()  
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                                  scriptLine = scriptLine + 1
                                  
while game_status == 'chooseName':
        win = pygame.display.set_mode((800,600))
        win.blit(background_image, [0, 0])
        win.blit(teacher,(450,260))
        qBoxWidth = 150
        qBoxLength = 50
        qBoxPosX = 50
        qboxPosy = 50
        pygame.draw.rect(win,(255,255,255), (qBoxPosX, qboxPosy, qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,255,255), (qBoxPosX, (qboxPosy + 100), qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,255,255), (qBoxPosX, (qboxPosy + 200), qBoxWidth, qBoxLength))
        font = pygame.font.Font('freesansbold.ttf', 32)
        win.blit(font.render(lines[questionLine + 1], True, (0,0,0)),(50,60))
        win.blit(font.render(lines[questionLine + 2], True, (0,0,0)),(50,160))
        win.blit(font.render(lines[questionLine + 3], True, (0,0,0)),(50,260))
        pygame.display.update()
        for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = event.pos
                    if 200 > mousex > 50  and 100 > mousey > 50:
                            name = str(lines[questionLine + 1])
                            scriptLine = 0
                            game_status = 'name choosen'
                    elif 200 > mousex > 50  and 200 > mousey > 150:
                            name = str(lines[questionLine + 2])
                            scriptLine = 0
                            game_status = 'name choosen'
                    elif 200 > mousex > 50  and 300 > mousey > 250:
                            name = str(lines[questionLine + 3])
                            scriptLine = 0   
                            game_status = 'name choosen'
                                          
while game_status == 'name choosen':
        win = pygame.display.set_mode((800,600))
        win.blit(background_image, [0, 0])
        teacher = pygame.transform.scale(pygame.image.load(filedir + '\pics\P3_Edogawa_Render.png'),(350, 450))
        #ripped from: Persona 3 FES(Playstation 2) [Video game]. (2006). Tokyo, Japan: Atlus Sega.
        win.blit(teacher,(450,260))
        script = open(filedir + '/script/' + game_status + '.txt', 'r')
        lines = script.readlines()
        font = pygame.font.Font('freesansbold.ttf', 32)
        try:
                text = font.render(str(lines[scriptLine]), True, (0,0,0))
                if 'insName' in str(lines[scriptLine]):
                        namedLine = (str(lines[scriptLine]).replace('insName', name))
                        text = font.render(namedLine, True, (0,0,0))
                        win.blit(text,(50,50))
                        pygame.display.update()
                        for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_SPACE:
                                                scriptLine = scriptLine + 1
                else:
                        win.blit(text,(50,50))
                        pygame.display.update()
                        for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_SPACE:
                                                scriptLine = scriptLine + 1
        except IndexError:
                game_status = 'Exam Hall'
                scriptLine = 0
        
while game_status == 'Exam Hall':
        win = pygame.display.set_mode((800,600))
        background_image = pygame.image.load(filedir + str('\\pics\\exam hall.png'))
        win.blit(background_image, [0, 0])
        teacher = pygame.transform.scale(pygame.image.load(filedir + '\pics\exam_teacher.png'), (300, 450))
        #ripped from: Persona 3 FES(Playstation 2) [Video game]. (2006). Tokyo, Japan: Atlus Sega.
        win.blit(teacher,(450,260))
        script = open(filedir + '/script/' + game_status + '.txt', 'r')
        lines = script.readlines()
        font = pygame.font.Font('freesansbold.ttf', 32)
        try:
                text = font.render(str(lines[scriptLine]), True, (255,255,255))
                if 'insName' in str(lines[scriptLine]):
                        namedLine = (str(lines[scriptLine]).replace('insName', name))
                        text = font.render(namedLine.strip('\n'), True, (255,255,255))
                        win.blit(text,(50,50))
                        pygame.display.update()
                else:
                        win.blit(text,(50,50))
                        pygame.display.update()
                        
        except IndexError:
                game_status = 'Exam Teacher Mood'
                scriptLine = 0
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                                  scriptLine = scriptLine + 1
while game_status == 'Exam Teacher Mood':
        script = open(filedir + '/script/' + game_status + '.txt', 'r')
        questionLine = 0
        lines = script.readlines()
        win = pygame.display.set_mode((800,600))
        win.blit(teacher,(450,260))
        win.blit(background_image, [0, 0])
        qBoxWidth = 500
        qBoxLength = 50
        qBoxPosX = 50
        qboxPosy = 50
        pygame.draw.rect(win,(255,255,255), (qBoxPosX, qboxPosy, qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,255,255), (qBoxPosX, (qboxPosy + 100), qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,255,255), (qBoxPosX, (qboxPosy + 200), qBoxWidth, qBoxLength))
        font = pygame.font.Font('freesansbold.ttf', 32)
        win.blit(font.render(lines[questionLine + 1], True, (0,0,0)),(50,60))
        win.blit(font.render(lines[questionLine + 2], True, (0,0,0)),(50,160))
        win.blit(font.render(lines[questionLine + 3], True, (0,0,0)),(50,260))
        pygame.display.update()
        for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = event.pos
                    if 500 > mousex > 50  and 100 > mousey > 50:
                            name = str(lines[questionLine + 1])
                            game_status = 'ExamTeach'
                            TeacherMood = 'Angry'
                            scriptLine = 0
                    elif 500 > mousex > 50  and 200 > mousey > 150:
                            name = str(lines[questionLine + 2])
                            game_status = 'ExamTeach'
                            TeacherMood = 'Neutral'
                            scriptLine = 3
                    elif 500 > mousex > 50  and 300 > mousey > 250:
                            name = str(lines[questionLine + 3])
                            game_status = 'ExamTeach'
                            TeacherMood = 'Disappointed'
                            scriptLine = 6
                            
while game_status == 'ExamTeach':
        win = pygame.display.set_mode((800,600))
        win.blit(teacher,(450,260))
        win.blit(background_image, [0, 0])
        script = open(filedir + '/script/' + game_status + '.txt', 'r')
        lines = script.readlines()
        font = pygame.font.Font('freesansbold.ttf', 32)
        if TeacherMood == 'Angry':
                if scriptLine == 2:
                        game_status = 'Exam start'
                        scriptLine = 0
                else:
                        text = font.render(str(lines[scriptLine]), True, (255,255,255))
                        if 'insName' in str(lines[scriptLine]):
                                namedLine = (str(lines[scriptLine]).replace('insName', name))
                                text = font.render(namedLine.strip('\n'), True, (255,255,255))
                                win.blit(text,(50,50))
                                pygame.display.update()
                        else:
                                win.blit(text,(50,50))
                                pygame.display.update()
        if TeacherMood == 'Neutral':
                if scriptLine == 5:
                        game_status = 'Exam start'
                        scriptLine = 0
                else:
                        text = font.render(str(lines[scriptLine]), True, (255,255,255))
                        if 'insName' in str(lines[scriptLine]):
                                namedLine = (str(lines[scriptLine]).replace('insName', name))
                                text = font.render(namedLine.strip('\n'), True, (255,255,255))
                                win.blit(text,(50,50))
                                pygame.display.update()
                        else:
                                win.blit(text,(50,50))
                                pygame.display.update()
                                
        if TeacherMood == 'Disappointed':
                if scriptLine == 8:
                        game_status = 'Exam start'
                        scriptLine = 0
                        
                else:
                        text = font.render(str(lines[scriptLine]), True, (255,255,255))
                        if 'insName' in str(lines[scriptLine]):
                                namedLine = (str(lines[scriptLine]).replace('insName', name))
                                text = font.render(namedLine.strip('\n'), True, (255,255,255))
                                win.blit(text,(50,50))
                                pygame.display.update()
                        else:
                                win.blit(text,(50,50))
                                pygame.display.update()
                
        
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                                scriptLine = scriptLine + 1


pygame.mixer.music.stop()
pygame.mixer.music.load(filedir + '\music\So Boring - Persona 5.mp3')
#Meguro, S. (2017). Persona 5 Original Soundtrack: So Boring [CD]. Tokyo: Atlus.
pygame.mixer.music.play(-1)
while game_status == 'Exam start':
        win = pygame.display.set_mode((800,600))
        text = font.render('Exam started', True, (0,0,0))
        win.blit(text,(250,260))
        script = open(filedir + '/script/' + game_status + '.txt', 'r')
        lines = script.readlines()
        font = pygame.font.Font('C:\WINDOWS\FONTS\LHANDW.TTF', 32)
        background_image = pygame.image.load(filedir + str('\\pics\\paperback.png'))
        win.blit(background_image, [0, 0])
        pygame.display.update()
        try:
                text = font.render(str(lines[scriptLine]), True, (0,0,0))
                if 'insName' in str(lines[scriptLine]):
                        namedLine = (str(lines[scriptLine]).replace('insName', name))
                        text = font.render(namedLine.strip('\n'), True, (0,0,0))
                        win.blit(text,(50,250))
                        pygame.display.update()
                else:
                        win.blit(text,(50,250))
                        pygame.display.update()
                        
        except IndexError:
                game_status = 'Exam Question 1'
                scriptLine = 0
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                                  scriptLine = scriptLine + 1


rightJingle = pygame.mixer.Sound(filedir + '\music\Persona 4 - Social Link Jingle.wav')
#ripped from: Persona 4 Golden (PC/Steam version) [Video game]. (2020). Tokyo, Japan: Atlus Sega.
wrongJingle = pygame.mixer.Sound(filedir + '\music\Turning Page - Sound Effect .wav') 
#sourced from: GFX Sounds. (2018). Turning Page - Sound Effect [HD] [Video]. Retrieved from https://www.youtube.com/watch?v=tuHaY1lwlEQ

while game_status == 'Exam Question 1':     
        while generator != 1:
                script = open(filedir + '/script/Exam questions/' + game_status +'.txt', 'r')
                lines = script.readlines()
                randNo = random.randint(0,2)
                questionsList = lines[randNo].split(', ')
                generator = 1
        win = pygame.display.set_mode((800,600))
        win.blit(background_image, [0, 0])
        qBoxWidth = 500
        qBoxLength = 50
        qBoxPosX = 50
        qboxPosy = 330
        pygame.draw.rect(win,(255,255,255), (qBoxPosX, qboxPosy, qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,255,255), (qBoxPosX, (qboxPosy + 100), qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,255,255), (qBoxPosX, (qboxPosy + 200), qBoxWidth, qBoxLength))
        font = pygame.font.Font('freesansbold.ttf', 32)
        win.blit(font.render(questionsList[0], True, (0,0,0)),(50,230))
        questionImg = pygame.transform.scale(pygame.image.load(filedir + '/pics/' + questionsList[5].rstrip('\n')), (269, 187))
        win.blit(questionImg,(50,25))
        if ' - right' in questionsList[1]:
                rightAnswer = questionsList[1].replace(" - right", "")
                win.blit(font.render(questionsList[1].replace(" - right", ""), True, (0,0,0)),(50,330))
                rightAnswerNo = 1
        else:
                win.blit(font.render(questionsList[1], True, (0,0,0)),(50,330))

        if ' - right' in questionsList[2]:
                rightAnswer = questionsList[2].replace(" - right", "")
                win.blit(font.render(questionsList[2].replace(" - right", ""), True, (0,0,0)),(50,430))
                rightAnswerNo = 2
        else:
                win.blit(font.render(questionsList[2], True, (0,0,0)),(50,430))
                
        if ' - right' in questionsList[3]:
                rightAnswer = questionsList[3].replace(" - right", "")
                win.blit(font.render(questionsList[3].replace(" - right", ""), True, (0,0,0)),(50,530))
                rightAnswerNo = 3
        else:
                win.blit(font.render(questionsList[3], True, (0,0,0)),(50,530))
                
        pygame.display.update()
        for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = event.pos  
                    if 500 > mousex > 50  and (qboxPosy + 50) > mousey > qboxPosy:
                        if rightAnswerNo == 1:
                                rightJingle.play(0)
                                generator = 0 
                                ExamScore = ExamScore + int(questionsList[4])
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                game_status = 'Exam Question 2'
                        else:
                                wrongJingle.play(0)
                                generator = 0 
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                game_status = 'Exam Question 2'
                                
                            
                    elif 500 > mousex > 50  and ((qboxPosy + 100) + 50) > mousey > (qboxPosy + 100):
                        if rightAnswerNo == 2:
                                rightJingle.play(0)
                                generator = 0 
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                ExamScore = ExamScore + int(questionsList[4])
                                game_status = 'Exam Question 2'
                        else:
                                wrongJingle.play(0)
                                generator = 0 
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                game_status = 'Exam Question 2'
                            
                    elif 500 > mousex > 50  and ((qboxPosy + 200) + 50) > mousey > (qboxPosy + 200):
                        if rightAnswerNo == 3:
                                rightJingle.play(0)
                                generator = 0 
                                ExamScore = ExamScore + int(questionsList[4])
                                MaxExamScore = MaxExamScore + int(questionsList[4]) 
                                game_status = 'Exam Question 2'
                        else:
                                wrongJingle.play(0)
                                generator = 0 
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                game_status = 'Exam Question 2'
#Pictures taken from:
#Python logo: Welcome to Python.org. (2001). Retrieved 16 October 2020, from https://www.python.org/
#SQL logo: Sql Server Logo - Unlimited Download. cleanpng.com. Retrieved 18 October 2020, from https://www.cleanpng.com/png-microsoft-sql-server-mysql-database-logo-2447831/
#Optical Illusion: Natalia, J. 10 Fun Visual Brain Teasers You Will Want To Share. Retrieved 18 October 2020, from https://www.ba-bamail.com/content.aspx?emailid=32451
                                
while game_status == 'Exam Question 2':
        while generator != 1:
                script = open(filedir + '/script/Exam questions/' + game_status +'.txt', 'r')
                lines = script.readlines()
                randNo = random.randint(0,2)
                questionsList = lines[randNo].split(', ')
                generator = 1
        win = pygame.display.set_mode((800,600))
        win.blit(background_image, [0, 0])
        qBoxWidth = 500
        qBoxLength = 50
        qBoxPosX = 50
        qboxPosy = 330
        pygame.draw.rect(win,(255,255,255), (qBoxPosX, qboxPosy, qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,255,255), (qBoxPosX, (qboxPosy + 100), qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,255,255), (qBoxPosX, (qboxPosy + 200), qBoxWidth, qBoxLength))
        font = pygame.font.Font('freesansbold.ttf', 32)
        win.blit(font.render(questionsList[0], True, (0,0,0)),(50,230))
        questionImg = pygame.transform.scale(pygame.image.load(filedir + '/pics/' + questionsList[5].rstrip('\n')), (269, 187))
        win.blit(questionImg,(50,25))
        if ' - right' in questionsList[1]:
                rightAnswer = questionsList[1].replace(" - right", "")
                win.blit(font.render(questionsList[1].replace(" - right", ""), True, (0,0,0)),(50,330))
                rightAnswerNo = 1
        else:
                win.blit(font.render(questionsList[1], True, (0,0,0)),(50,330))

        if ' - right' in questionsList[2]:
                rightAnswer = questionsList[2].replace(" - right", "")
                win.blit(font.render(questionsList[2].replace(" - right", ""), True, (0,0,0)),(50,430))
                rightAnswerNo = 2
        else:
                win.blit(font.render(questionsList[2], True, (0,0,0)),(50,430))
                
        if ' - right' in questionsList[3]:
                rightAnswer = questionsList[3].replace(" - right", "")
                win.blit(font.render(questionsList[3].replace(" - right", ""), True, (0,0,0)),(50,530))
                rightAnswerNo = 3
        else:
                win.blit(font.render(questionsList[3], True, (0,0,0)),(50,530))
                
        pygame.display.update()
        for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = event.pos
                    if 500 > mousex > 50  and (qboxPosy + 50) > mousey > qboxPosy:
                        if rightAnswerNo == 1:
                                rightJingle.play(0)
                                ExamScore = ExamScore + int(questionsList[4])
                                generator = 0
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                game_status = 'Exam Question 3'
                        else:
                                wrongJingle.play(0)
                                generator = 0
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                game_status = 'Exam Question 3'
                                
                            
                    elif 500 > mousex > 50  and ((qboxPosy + 100) + 50) > mousey > (qboxPosy + 100):
                        if rightAnswerNo == 2:
                                rightJingle.play(0)
                                ExamScore = ExamScore + int(questionsList[4])
                                generator = 0
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                game_status = 'Exam Question 3'
                        else:
                                wrongJingle.play(0)
                                generator = 0
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                game_status = 'Exam Question 3'
                            
                    elif 500 > mousex > 50  and ((qboxPosy + 200) + 50) > mousey > (qboxPosy + 200):
                        if rightAnswerNo == 3:
                                rightJingle.play(0)
                                ExamScore = ExamScore + int(questionsList[4])
                                generator = 0
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                game_status = 'Exam Question 4'
                        else:
                                wrongJingle.play(0)
                                generator = 0
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                game_status = 'Exam Question 4'

#Pictures taken from:
#Python logo: Welcome to Python.org. (2001). Retrieved 16 October 2020, from https://www.python.org/
#SQL logo: Sql Server Logo - Unlimited Download. cleanpng.com. Retrieved 18 October 2020, from https://www.cleanpng.com/png-microsoft-sql-server-mysql-database-logo-2447831/
#Optical Illusion: Natalia, J. 10 Fun Visual Brain Teasers You Will Want To Share. Retrieved 18 October 2020, from https://www.ba-bamail.com/content.aspx?emailid=32451
                                                          

while game_status == 'Exam Question 3':
        while generator != 1:
                script = open(filedir + '/script/Exam questions/' + game_status +'.txt', 'r')
                lines = script.readlines()
                randNo = random.randint(0,2)
                questionsList = lines[randNo].split(', ')
                generator = 1
        win = pygame.display.set_mode((800,600))
        win.blit(background_image, [0, 0])
        qBoxWidth = 500
        qBoxLength = 50
        qBoxPosX = 50
        qboxPosy = 330
        pygame.draw.rect(win,(255,255,255), (qBoxPosX, qboxPosy, qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,255,255), (qBoxPosX, (qboxPosy + 100), qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,255,255), (qBoxPosX, (qboxPosy + 200), qBoxWidth, qBoxLength))
        font = pygame.font.Font('freesansbold.ttf', 32)
        win.blit(font.render(questionsList[0], True, (0,0,0)),(50,230))
        questionImg = pygame.transform.scale(pygame.image.load(filedir + '/pics/' + questionsList[5].rstrip('\n')), (269, 187))
        win.blit(questionImg,(50,25))
        if ' - right' in questionsList[1]:
                rightAnswer = questionsList[1].replace(" - right", "")
                win.blit(font.render(questionsList[1].replace(" - right", ""), True, (0,0,0)),(50,330))
                rightAnswerNo = 1
        else:
                win.blit(font.render(questionsList[1], True, (0,0,0)),(50,330))

        if ' - right' in questionsList[2]:
                rightAnswer = questionsList[2].replace(" - right", "")
                win.blit(font.render(questionsList[2].replace(" - right", ""), True, (0,0,0)),(50,430))
                rightAnswerNo = 2
        else:
                win.blit(font.render(questionsList[2], True, (0,0,0)),(50,430))
                
        if ' - right' in questionsList[3]:
                rightAnswer = questionsList[3].replace(" - right", "")
                win.blit(font.render(questionsList[3].replace(" - right", ""), True, (0,0,0)),(50,530))
                rightAnswerNo = 3
        else:
                win.blit(font.render(questionsList[3], True, (0,0,0)),(50,530))
                
        pygame.display.update()
        for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = event.pos  
                    if 500 > mousex > 50  and (qboxPosy + 50) > mousey > qboxPosy:
                        if rightAnswerNo == 1:
                                rightJingle.play(0)
                                ExamScore = ExamScore + int(questionsList[4])
                                generator = 0
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                game_status = 'Exam Question 4'
                        else:
                                wrongJingle.play(0)
                                generator = 0
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                game_status = 'Exam Question 4'
                                
                            
                    elif 500 > mousex > 50  and ((qboxPosy + 100) + 50) > mousey > (qboxPosy + 100):
                        if rightAnswerNo == 2:
                                rightJingle.play(0)
                                ExamScore = ExamScore + int(questionsList[4])
                                generator = 0
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                game_status = 'Exam Question 4'
                        else:
                                wrongJingle.play(0)
                                generator = 0
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                game_status = 'Exam Question 4'
                            
                    elif 500 > mousex > 50  and ((qboxPosy + 200) + 50) > mousey > (qboxPosy + 200):
                        if rightAnswerNo == 3:
                                rightJingle.play(0)
                                ExamScore = ExamScore + int(questionsList[4])
                                generator = 0
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                game_status = 'Exam Question 4'
                        else:
                                wrongJingle.play(0)
                                generator = 0
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                game_status = 'Exam Question 4'

#Pictures taken Portugal. (2020). Retrieved 18 October 2020, from https://en.wikipedia.org/wiki/Portugal    
#Pictures taken Spain. (2020). Retrieved 18 October 2020, from https://en.wikipedia.org/wiki/Spain
#Pictures taken Canada. (2020). Retrieved 18 October 2020, from https://en.wikipedia.org/wiki/Canada                                                        

while game_status == 'Exam Question 4':
        while generator != 1:
                script = open(filedir + '/script/Exam questions/' + game_status +'.txt', 'r')
                lines = script.readlines()
                randNo = random.randint(0,2)
                questionsList = lines[randNo].split(', ')
                generator = 1
        win = pygame.display.set_mode((800,600))
        win.blit(background_image, [0, 0])
        qBoxWidth = 500
        qBoxLength = 50
        qBoxPosX = 50
        qboxPosy = 330
        pygame.draw.rect(win,(255,255,255), (qBoxPosX, qboxPosy, qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,255,255), (qBoxPosX, (qboxPosy + 100), qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,255,255), (qBoxPosX, (qboxPosy + 200), qBoxWidth, qBoxLength))
        font = pygame.font.Font('freesansbold.ttf', 32)
        win.blit(font.render(questionsList[0], True, (0,0,0)),(50,230))
        questionImg = pygame.transform.scale(pygame.image.load(filedir + '/pics/' + questionsList[5].rstrip('\n')), (269, 187))
        win.blit(questionImg,(50,25))
        if ' - right' in questionsList[1]:
                rightAnswer = questionsList[1].replace(" - right", "")
                win.blit(font.render(questionsList[1].replace(" - right", ""), True, (0,0,0)),(50,330))
                rightAnswerNo = 1
        else:
                win.blit(font.render(questionsList[1], True, (0,0,0)),(50,330))

        if ' - right' in questionsList[2]:
                rightAnswer = questionsList[2].replace(" - right", "")
                win.blit(font.render(questionsList[2].replace(" - right", ""), True, (0,0,0)),(50,430))
                rightAnswerNo = 2
        else:
                win.blit(font.render(questionsList[2], True, (0,0,0)),(50,430))
                
        if ' - right' in questionsList[3]:
                rightAnswer = questionsList[3].replace(" - right", "")
                win.blit(font.render(questionsList[3].replace(" - right", ""), True, (0,0,0)),(50,530))
                rightAnswerNo = 3
        else:
                win.blit(font.render(questionsList[3], True, (0,0,0)),(50,530))
                
        pygame.display.update()
        for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = event.pos 
                    if 500 > mousex > 50  and (qboxPosy + 50) > mousey > qboxPosy:
                        if rightAnswerNo == 1:
                                rightJingle.play(0)
                                ExamScore = ExamScore + int(questionsList[4])
                                generator = 0
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                game_status = 'Exam Question 5'
                        else:
                                wrongJingle.play(0)
                                generator = 0
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                game_status = 'Exam Question 5'
                                
                            
                    elif 500 > mousex > 50  and ((qboxPosy + 100) + 50) > mousey > (qboxPosy + 100):
                        if rightAnswerNo == 2:
                                rightJingle.play(0)
                                ExamScore = ExamScore + int(questionsList[4])
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                generator = 0
                                game_status = 'Exam Question 5'
                        else:
                                wrongJingle.play(0)
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                generator = 0
                                game_status = 'Exam Question 5'
                            
                    elif 500 > mousex > 50  and ((qboxPosy + 200) + 50) > mousey > (qboxPosy + 200):
                        if rightAnswerNo == 3:
                                rightJingle.play(0)
                                ExamScore = ExamScore + int(questionsList[4])
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                generator = 0
                                game_status = 'Exam Question 5'
                        else:
                                wrongJingle.play(0)
                                generator = 0
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                game_status = 'Exam Question 5'

#Pictures taken Portugal. (2020). Retrieved 18 October 2020, from https://en.wikipedia.org/wiki/Portugal    
#Pictures taken Spain. (2020). Retrieved 18 October 2020, from https://en.wikipedia.org/wiki/Spain
#Pictures taken Canada. (2020). Retrieved 18 October 2020, from https://en.wikipedia.org/wiki/Canada   

while game_status == 'Exam Question 5':
        while generator != 1:
                script = open(filedir + '/script/Exam questions/' + game_status +'.txt', 'r')
                lines = script.readlines()
                randNo = random.randint(0,2)
                questionsList = lines[randNo].split(', ')
                generator = 1
        win = pygame.display.set_mode((800,600))
        win.blit(background_image, [0, 0])
        qBoxWidth = 500
        qBoxLength = 50
        qBoxPosX = 50
        qboxPosy = 330
        pygame.draw.rect(win,(255,255,255), (qBoxPosX, qboxPosy, qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,255,255), (qBoxPosX, (qboxPosy + 100), qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,255,255), (qBoxPosX, (qboxPosy + 200), qBoxWidth, qBoxLength))
        font = pygame.font.Font('freesansbold.ttf', 32)
        win.blit(font.render(questionsList[0], True, (0,0,0)),(50,230))
        questionImg = pygame.transform.scale(pygame.image.load(filedir + '/pics/' + questionsList[5].rstrip('\n')), (269, 187))
        win.blit(questionImg,(50,25))
        if ' - right' in questionsList[1]:
                rightAnswer = questionsList[1].replace(" - right", "")
                win.blit(font.render(questionsList[1].replace(" - right", ""), True, (0,0,0)),(50,330))
                rightAnswerNo = 1
        else:
                win.blit(font.render(questionsList[1], True, (0,0,0)),(50,330))

        if ' - right' in questionsList[2]:
                rightAnswer = questionsList[2].replace(" - right", "")
                win.blit(font.render(questionsList[2].replace(" - right", ""), True, (0,0,0)),(50,430))
                rightAnswerNo = 2
        else:
                win.blit(font.render(questionsList[2], True, (0,0,0)),(50,430))
                
        if ' - right' in questionsList[3]:
                rightAnswer = questionsList[3].replace(" - right", "")
                win.blit(font.render(questionsList[3].replace(" - right", ""), True, (0,0,0)),(50,530))
                rightAnswerNo = 3
        else:
                win.blit(font.render(questionsList[3], True, (0,0,0)),(50,530))
                
        pygame.display.update()
        for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = event.pos  
                    if 500 > mousex > 50  and (qboxPosy + 50) > mousey > qboxPosy:
                        if rightAnswerNo == 1:
                                rightJingle.play(0)
                                scriptLine = 0
                                ExamScore = ExamScore + int(questionsList[4])
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                game_status = 'End Exam'
                        else:
                                wrongJingle.play(0)
                                scriptLine = 0
                                game_status = 'End Exam'
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                
                            
                    elif 500 > mousex > 50  and ((qboxPosy + 100) + 50) > mousey > (qboxPosy + 100):
                        if rightAnswerNo == 2:
                                rightJingle.play(0)
                                scriptLine = 0
                                ExamScore = ExamScore + int(questionsList[4])
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                game_status = 'End Exam'
                        else:
                                wrongJingle.play(0)
                                scriptLine = 0
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                game_status = 'End Exam'
                            
                    elif 500 > mousex > 50  and ((qboxPosy + 200) + 50) > mousey > (qboxPosy + 200):
                        if rightAnswerNo == 3:
                                rightJingle.play(0)
                                scriptLine = 0
                                ExamScore = ExamScore + int(questionsList[4])
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                game_status = 'End Exam'
                        else:
                                wrongJingle.play(0)
                                scriptLine = 0
                                MaxExamScore = MaxExamScore + int(questionsList[4])
                                game_status = 'End Exam'    

#liberty: Hudson, M. (2020). Why Is the Statue of Liberty a Woman?. Retrieved 18 October 2020, from https://www.britannica.com/story/why-is-the-statue-of-liberty-a-woman
#taj: Centre, U. (1992). Taj Mahal. Retrieved 18 October 2020, from https://whc.unesco.org/en/list/252/
#Juche: Juche Tower guide, North Korea. Retrieved 18 October 2020, from https://www.koreakonsult.com/Attraction_Pyongyang_juche_tower_eng.html

pygame.mixer.music.stop()  
pygame.mixer.music.load(filedir + '\music\My Homie - Persona 5.mp3')
#Meguro, S. (2017). Persona 5 Original Soundtrack: My Homie [CD]. Tokyo: Atlus.
pygame.mixer.music.play(-1)

while game_status == 'End Exam':
        win = pygame.display.set_mode((800,600))
        background_image = pygame.image.load(filedir + str('\\pics\\exam hall.png'))
        win.blit(background_image, [0, 0])
        script = open(filedir + '\\script\\' + game_status + '.txt', 'r')
        lines = script.readlines()
        font = pygame.font.Font('freesansbold.ttf', 32)
        try:
                text = font.render(str(lines[scriptLine]).strip('\n'), True, (255,255,255))
        except IndexError:
                 scriptLine = 0
                 game_status = 'Exam results'
        
        win.blit(text,(50,50))
        questionLine = scriptLine
        teacher = pygame.transform.scale(pygame.image.load(filedir + '\pics\exam_teacher.png'), (350, 450))
        win.blit(teacher,(450,260))
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                                        scriptLine = scriptLine + 1
#Pics taken from:
# Donkey:Cyprus donkey. (2020). Retrieved 18 October 2020, from https://en.wikipedia.org/wiki/Cyprus_donkey                                    
scriptLine = 0
 
while game_status == 'Exam results':
        win = pygame.display.set_mode((800,600))
        win.blit(background_image, [0, 0])
        script = open(filedir + '\\script\\' + game_status + '.txt', 'r')
        lines = script.readlines()
        font = pygame.font.Font('freesansbold.ttf', 32)
        try:
                namedLine = str(lines[scriptLine])
                text = font.render(str(lines[scriptLine]).strip('\n'), True, (255,255,255))
        except IndexError:
                 scriptLine = 0
                 game_status = 'one week passes'
        win.blit(text,(50,50))
        questionLine = scriptLine
        teacher = pygame.transform.scale(pygame.image.load(filedir + '\pics\exam_teacher.png'), (350, 450))
        win.blit(teacher,(450,260))
        pygame.display.update()  
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                                        scriptLine = scriptLine + 1
                                        

while game_status == 'one week passes':
        win = pygame.display.set_mode((800,600))
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("One week passes", True, (255,255,255))
        win.blit(text,(50,50))
        pygame.display.update()  
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                                if (ExamScore/MaxExamScore) > 0.74:
                                        Feelings = 'Confident'
                                        game_status = 'Feels'
                                        scriptLine = 0
                                        generator = 0
                                elif (ExamScore/MaxExamScore) > 0.49:
                                        Feelings = 'Okay'
                                        game_status = 'Feels'
                                        scriptLine = 0
                                        generator = 0
                                elif (ExamScore/MaxExamScore) > 0.24:
                                        Feelings = 'Not so confident'
                                        game_status = 'Feels'
                                        scriptLine = 0
                                        generator = 0

while game_status == 'Feels':
        win = pygame.display.set_mode((800,600))
        win.blit(background_image, [0, 0])
        if  lines[scriptLine].startswith('Feel') == True:
                if Feelings == 'Confident':
                        scriptLine = 4
                        generator = 1
                elif Feelings == 'Okay':
                        scriptLine = 5
                        generator = 1
                elif Feelings == 'Not so confident':
                        scriptLine = 6
                        generator = 1
        script = open(filedir + '\\script\\' + game_status + '.txt', 'r')
        lines = script.readlines()
        text = font.render(str(lines[scriptLine]).strip('\n'), True, (255,255,255))
        font = pygame.font.Font('freesansbold.ttf', 32)
        win.blit(text,(50,50))
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                                        scriptLine = scriptLine + 1
                                        if generator == 1:
                                                scriptLine = 0
                                                game_status = 'Results'
        
                


while game_status == 'Results':
        win = pygame.display.set_mode((800,600))
        background_image = pygame.image.load(filedir + str('\\pics\\exam hall.png'))
        win.blit(background_image, [0, 0])
        script = open(filedir + '\\script\\' + game_status + '.txt', 'r')
        lines = script.readlines()
        font = pygame.font.Font('freesansbold.ttf', 32)
        try:
                textHolder = str(lines[scriptLine]).strip('\n')
                if textHolder.startswith('insExam') == True:
                        textholder2 = textHolder.replace('insExam', str(ExamScore) + '/'+ str(MaxExamScore))
                        text = font.render(textholder2, True, (255,255,255))
                else:        
                        text = font.render(textHolder, True, (255,255,255))
        except IndexError:
                 scriptLine = 0
                 quit()        
        win.blit(text,(50,50))
        questionLine = scriptLine
        teacher = pygame.transform.scale(pygame.image.load(filedir + '\pics\exam_teacher.png'), (350, 450))
        win.blit(teacher,(450,260))
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                                        scriptLine = scriptLine + 1
