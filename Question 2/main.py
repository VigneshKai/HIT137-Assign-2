import pygame
import os
import random
filepath = os.path.abspath(__file__)
filedir = os.path.dirname(filepath)
pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.mixer.music.load(filedir + str('\Music\Persona 3 OST - During the Test (Extended).mp3'))
game_status = 'start'
scriptLine = 0
questionLine = 0
name = ''
questionsList = []
TeacherMood = ''
generator = 0
rightAnswer = ''
rightAnswerNo= 0
ExamScore = 0


while game_status == 'start':
        win = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Exam Simulator")
        x = 250
        y = 250
        width = 350
        height = 50
        vol = 5
        pygame.draw.rect(win,(255,0,0), (x, y, width, height))
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Exam Simulator', True, (255,255,255))
        win.blit(text,(250,260))
        pygame.display.update()
        for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = event.pos
                    print(str(mousex) +','+ str(mousey))
                    print(game_status)  
                    if 550 > mousex > 250  and 300 > mousey > 250:
                            game_status = 'intro'
                            pygame.mixer.music.play(-1)


while game_status == 'intro':
        win = pygame.display.set_mode((800,600))
        script = open(filedir + '/script/' + game_status + '.txt', 'r')
        lines = script.readlines()
        if lines[questionLine].startswith('Question'):
                theQuestion = (lines[questionLine][13:])
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render(str(theQuestion), True, (255,255,255))
                win.blit(text,(50,50))
                questions = lines[questionLine][10:].split()[0]
                game_status = 'chooseName'
                
        else:
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render(str(lines[scriptLine]), True, (255,255,255))
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
        win.blit(teacher,(450,260))
        qBoxWidth = 150
        qBoxLength = 50
        qBoxPosX = 50
        qboxPosy = 50
        pygame.draw.rect(win,(255,0,0), (qBoxPosX, qboxPosy, qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,0,0), (qBoxPosX, (qboxPosy + 100), qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,0,0), (qBoxPosX, (qboxPosy + 200), qBoxWidth, qBoxLength))
        font = pygame.font.Font('freesansbold.ttf', 32)
        win.blit(font.render(lines[questionLine + 1], True, (255,255,255)),(50,60))
        win.blit(font.render(lines[questionLine + 2], True, (255,255,255)),(50,160))
        win.blit(font.render(lines[questionLine + 3], True, (255,255,255)),(50,260))
        pygame.display.update()
        for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = event.pos
                    print(str(mousex) +','+ str(mousey))
                    print(game_status)  
                    if 200 > mousex > 50  and 100 > mousey > 50:
                            name = str(lines[questionLine + 1])
                            game_status = 'name choosen'
                            scriptLine = 0
                    elif 200 > mousex > 50  and 200 > mousey > 150:
                            name = str(lines[questionLine + 2])
                            game_status = 'name choosen'
                            scriptLine = 0
                    elif 200 > mousex > 50  and 300 > mousey > 250:
                            name = str(lines[questionLine + 3])
                            game_status = 'name choosen'
                            scriptLine = 0
                            
while game_status == 'name choosen':
        win = pygame.display.set_mode((800,600))
        teacher = pygame.transform.scale(pygame.image.load(filedir + '\pics\P3_Edogawa_Render.png'), (350, 450))
        win.blit(teacher,(450,260))
        script = open(filedir + '/script/' + game_status + '.txt', 'r')
        lines = script.readlines()
        font = pygame.font.Font('freesansbold.ttf', 32)
        try:
                text = font.render(str(lines[scriptLine]), True, (255,255,255))
                if 'insName' in str(lines[scriptLine]):
                        namedLine = (str(lines[scriptLine]).replace('insName', name))
                        text = font.render(namedLine, True, (255,255,255))
                        win.blit(text,(50,50))
                        pygame.display.update()
                else:
                        win.blit(text,(50,50))
                        pygame.display.update()
        except IndexError:
                game_status = 'Exam Hall'
                scriptLine = 0
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                                  scriptLine = scriptLine + 1
while game_status == 'Exam Hall':
        win = pygame.display.set_mode((800,600))
        teacher = pygame.transform.scale(pygame.image.load(filedir + '\pics\exam_teacher.png'), (300, 450))
        win.blit(teacher,(450,260))
        script = open(filedir + '/script/' + game_status + '.txt', 'r')
        lines = script.readlines()
        font = pygame.font.Font('freesansbold.ttf', 32)
        try:
                text = font.render(str(lines[scriptLine]), True, (255,255,255))
                if 'insName' in str(lines[scriptLine]):
                        namedLine = (str(lines[scriptLine]).replace('insName', name))
                        text = font.render(namedLine, True, (255,255,255))
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
        qBoxWidth = 500
        qBoxLength = 50
        qBoxPosX = 50
        qboxPosy = 50
        pygame.draw.rect(win,(255,0,0), (qBoxPosX, qboxPosy, qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,0,0), (qBoxPosX, (qboxPosy + 100), qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,0,0), (qBoxPosX, (qboxPosy + 200), qBoxWidth, qBoxLength))
        font = pygame.font.Font('freesansbold.ttf', 32)
        win.blit(font.render(lines[questionLine + 1], True, (255,255,255)),(50,60))
        win.blit(font.render(lines[questionLine + 2], True, (255,255,255)),(50,160))
        win.blit(font.render(lines[questionLine + 3], True, (255,255,255)),(50,260))
        pygame.display.update()
        for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = event.pos
                    print(str(mousex) +','+ str(mousey))
                    print(game_status)  
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
                            TeacherMood = 'Disgust'
                            scriptLine = 6
                            
while game_status == 'ExamTeach':
        win = pygame.display.set_mode((800,600))
        win.blit(teacher,(450,260))
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
                                text = font.render(namedLine, True, (255,255,255))
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
                                text = font.render(namedLine, True, (255,255,255))
                                win.blit(text,(50,50))
                                pygame.display.update()
                        else:
                                win.blit(text,(50,50))
                                pygame.display.update()
                                
        if TeacherMood == 'Disgust':
                if scriptLine == 8:
                        game_status = 'Exam start'
                        scriptLine = 0
                        
                else:
                        text = font.render(str(lines[scriptLine]), True, (255,255,255))
                        if 'insName' in str(lines[scriptLine]):
                                namedLine = (str(lines[scriptLine]).replace('insName', name))
                                text = font.render(namedLine, True, (255,255,255))
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
pygame.mixer.music.play(-1)
while game_status == 'Exam start':
        font = pygame.font.Font('C:\WINDOWS\FONTS\LHANDW.TTF', 32)
        text = font.render('Exam started', True, (255,255,255))
        win.blit(text,(250,260))
        win = pygame.display.set_mode((800,600))
        script = open(filedir + '/script/' + game_status + '.txt', 'r')
        lines = script.readlines()
        font = pygame.font.Font('C:\WINDOWS\FONTS\LHANDW.TTF', 32)
        try:
                text = font.render(str(lines[scriptLine]), True, (255,255,255))
                if 'insName' in str(lines[scriptLine]):
                        namedLine = (str(lines[scriptLine]).replace('insName', name))
                        text = font.render(namedLine, True, (255,255,255))
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
wrongJingle = pygame.mixer.Sound(filedir + '\music\Turning Page - Sound Effect .wav')

                                  
while game_status == 'Exam Question 1':
        while generator != 1:
                script = open(filedir + '/script/Exam questions/' + game_status +'.txt', 'r')
                lines = script.readlines()
                randNo = random.randint(0,2)
                questionsList = lines[randNo].split(', ')
                generator = 1
                print(questionsList)
        win = pygame.display.set_mode((800,600))
        
        qBoxWidth = 500
        qBoxLength = 50
        qBoxPosX = 50
        qboxPosy = 330
        pygame.draw.rect(win,(255,0,0), (qBoxPosX, qboxPosy, qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,0,0), (qBoxPosX, (qboxPosy + 100), qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,0,0), (qBoxPosX, (qboxPosy + 200), qBoxWidth, qBoxLength))
        font = pygame.font.Font('freesansbold.ttf', 32)
        win.blit(font.render(questionsList[0], True, (255,255,255)),(50,230))
        questionImg = pygame.transform.scale(pygame.image.load(filedir + '/pics/' + questionsList[5].rstrip('\n')), (269, 187))
        win.blit(questionImg,(50,25))
        if ' - right' in questionsList[1]:
                rightAnswer = questionsList[1].replace(" - right", "")
                win.blit(font.render(questionsList[1].replace(" - right", ""), True, (255,255,255)),(50,330))
                rightAnswerNo = 1
        else:
                win.blit(font.render(questionsList[1], True, (255,255,255)),(50,330))

        if ' - right' in questionsList[2]:
                rightAnswer = questionsList[2].replace(" - right", "")
                win.blit(font.render(questionsList[2].replace(" - right", ""), True, (255,255,255)),(50,430))
                rightAnswerNo = 2
        else:
                win.blit(font.render(questionsList[2], True, (255,255,255)),(50,430))
                
        if ' - right' in questionsList[3]:
                rightAnswer = questionsList[3].replace(" - right", "")
                win.blit(font.render(questionsList[3].replace(" - right", ""), True, (255,255,255)),(50,530))
                rightAnswerNo = 3
        else:
                win.blit(font.render(questionsList[3], True, (255,255,255)),(50,530))
                
        pygame.display.update()
        for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = event.pos
                    print(str(mousex) +','+ str(mousey))
                    print(game_status)  
                    if 500 > mousex > 50  and (qboxPosy + 50) > mousey > qboxPosy:
                        if rightAnswerNo == 1:
                                rightJingle.play(0)
                                generator = 0 
                                ExamScore = ExamScore + int(questionsList[4])
                                game_status = 'Exam Question 2'
                        else:
                                wrongJingle.play(0)
                                generator = 0 
                                game_status = 'Exam Question 2'
                                
                            
                    elif 500 > mousex > 50  and ((qboxPosy + 100) + 50) > mousey > (qboxPosy + 100):
                        if rightAnswerNo == 2:
                                rightJingle.play(0)
                                generator = 0 
                                ExamScore = ExamScore + int(questionsList[4])
                                game_status = 'Exam Question 2'
                        else:
                                wrongJingle.play(0)
                                generator = 0 
                                game_status = 'Exam Question 2'
                            
                    elif 500 > mousex > 50  and ((qboxPosy + 200) + 50) > mousey > (qboxPosy + 200):
                        if rightAnswerNo == 3:
                                rightJingle.play(0)
                                generator = 0 
                                ExamScore = ExamScore + int(questionsList[4])
                                game_status = 'Exam Question 2'
                        else:
                                wrongJingle.play(0)
                                generator = 0 
                                game_status = 'Exam Question 2'
                                
                                
while game_status == 'Exam Question 2':
        while generator != 1:
                script = open(filedir + '/script/Exam questions/' + game_status +'.txt', 'r')
                lines = script.readlines()
                randNo = random.randint(0,2)
                questionsList = lines[randNo].split(', ')
                generator = 1
                print(questionsList)
        win = pygame.display.set_mode((800,600))
        
        qBoxWidth = 500
        qBoxLength = 50
        qBoxPosX = 50
        qboxPosy = 330
        pygame.draw.rect(win,(255,0,0), (qBoxPosX, qboxPosy, qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,0,0), (qBoxPosX, (qboxPosy + 100), qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,0,0), (qBoxPosX, (qboxPosy + 200), qBoxWidth, qBoxLength))
        font = pygame.font.Font('freesansbold.ttf', 32)
        win.blit(font.render(questionsList[0], True, (255,255,255)),(50,230))
        questionImg = pygame.transform.scale(pygame.image.load(filedir + '/pics/' + questionsList[5].rstrip('\n')), (269, 187))
        win.blit(questionImg,(50,25))
        if ' - right' in questionsList[1]:
                rightAnswer = questionsList[1].replace(" - right", "")
                win.blit(font.render(questionsList[1].replace(" - right", ""), True, (255,255,255)),(50,330))
                rightAnswerNo = 1
        else:
                win.blit(font.render(questionsList[1], True, (255,255,255)),(50,330))

        if ' - right' in questionsList[2]:
                rightAnswer = questionsList[2].replace(" - right", "")
                win.blit(font.render(questionsList[2].replace(" - right", ""), True, (255,255,255)),(50,430))
                rightAnswerNo = 2
        else:
                win.blit(font.render(questionsList[2], True, (255,255,255)),(50,430))
                
        if ' - right' in questionsList[3]:
                rightAnswer = questionsList[3].replace(" - right", "")
                win.blit(font.render(questionsList[3].replace(" - right", ""), True, (255,255,255)),(50,530))
                rightAnswerNo = 3
        else:
                win.blit(font.render(questionsList[3], True, (255,255,255)),(50,530))
                
        pygame.display.update()
        for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = event.pos
                    print(str(mousex) +','+ str(mousey))
                    print(game_status)  
                    if 500 > mousex > 50  and (qboxPosy + 50) > mousey > qboxPosy:
                        if rightAnswerNo == 1:
                                rightJingle.play(0)
                                ExamScore = ExamScore + int(questionsList[4])
                                generator = 0
                                game_status = 'Exam Question 3'
                        else:
                                wrongJingle.play(0)
                                generator = 0
                                game_status = 'Exam Question 3'
                                
                            
                    elif 500 > mousex > 50  and ((qboxPosy + 100) + 50) > mousey > (qboxPosy + 100):
                        if rightAnswerNo == 2:
                                rightJingle.play(0)
                                ExamScore = ExamScore + int(questionsList[4])
                                generator = 0
                                game_status = 'Exam Question 3'
                        else:
                                wrongJingle.play(0)
                                generator = 0
                                game_status = 'Exam Question 3'
                            
                    elif 500 > mousex > 50  and ((qboxPosy + 200) + 50) > mousey > (qboxPosy + 200):
                        if rightAnswerNo == 3:
                                rightJingle.play(0)
                                ExamScore = ExamScore + int(questionsList[4])
                                generator = 0
                                game_status = 'Exam Question 4'
                        else:
                                wrongJingle.play(0)
                                generator = 0
                                game_status = 'Exam Question 4'

                                                          

while game_status == 'Exam Question 3':
        while generator != 1:
                script = open(filedir + '/script/Exam questions/' + game_status +'.txt', 'r')
                lines = script.readlines()
                randNo = random.randint(0,2)
                questionsList = lines[randNo].split(', ')
                generator = 1
                print(questionsList)
        win = pygame.display.set_mode((800,600))
        
        qBoxWidth = 500
        qBoxLength = 50
        qBoxPosX = 50
        qboxPosy = 330
        pygame.draw.rect(win,(255,0,0), (qBoxPosX, qboxPosy, qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,0,0), (qBoxPosX, (qboxPosy + 100), qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,0,0), (qBoxPosX, (qboxPosy + 200), qBoxWidth, qBoxLength))
        font = pygame.font.Font('freesansbold.ttf', 32)
        win.blit(font.render(questionsList[0], True, (255,255,255)),(50,230))
        questionImg = pygame.transform.scale(pygame.image.load(filedir + '/pics/' + questionsList[5].rstrip('\n')), (269, 187))
        win.blit(questionImg,(50,25))
        if ' - right' in questionsList[1]:
                rightAnswer = questionsList[1].replace(" - right", "")
                win.blit(font.render(questionsList[1].replace(" - right", ""), True, (255,255,255)),(50,330))
                rightAnswerNo = 1
        else:
                win.blit(font.render(questionsList[1], True, (255,255,255)),(50,330))

        if ' - right' in questionsList[2]:
                rightAnswer = questionsList[2].replace(" - right", "")
                win.blit(font.render(questionsList[2].replace(" - right", ""), True, (255,255,255)),(50,430))
                rightAnswerNo = 2
        else:
                win.blit(font.render(questionsList[2], True, (255,255,255)),(50,430))
                
        if ' - right' in questionsList[3]:
                rightAnswer = questionsList[3].replace(" - right", "")
                win.blit(font.render(questionsList[3].replace(" - right", ""), True, (255,255,255)),(50,530))
                rightAnswerNo = 3
        else:
                win.blit(font.render(questionsList[3], True, (255,255,255)),(50,530))
                
        pygame.display.update()
        for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = event.pos
                    print(str(mousex) +','+ str(mousey))
                    print(game_status)  
                    if 500 > mousex > 50  and (qboxPosy + 50) > mousey > qboxPosy:
                        if rightAnswerNo == 1:
                                rightJingle.play(0)
                                ExamScore = ExamScore + int(questionsList[4])
                                generator = 0
                                game_status = 'Exam Question 4'
                        else:
                                wrongJingle.play(0)
                                generator = 0
                                game_status = 'Exam Question 4'
                                
                            
                    elif 500 > mousex > 50  and ((qboxPosy + 100) + 50) > mousey > (qboxPosy + 100):
                        if rightAnswerNo == 2:
                                rightJingle.play(0)
                                ExamScore = ExamScore + int(questionsList[4])
                                generator = 0
                                game_status = 'Exam Question 4'
                        else:
                                wrongJingle.play(0)
                                generator = 0
                                game_status = 'Exam Question 4'
                            
                    elif 500 > mousex > 50  and ((qboxPosy + 200) + 50) > mousey > (qboxPosy + 200):
                        if rightAnswerNo == 3:
                                rightJingle.play(0)
                                ExamScore = ExamScore + int(questionsList[4])
                                generator = 0
                                game_status = 'Exam Question 4'
                        else:
                                wrongJingle.play(0)
                                generator = 0
                                game_status = 'Exam Question 4'

                                

while game_status == 'Exam Question 4':
        while generator != 1:
                script = open(filedir + '/script/Exam questions/' + game_status +'.txt', 'r')
                lines = script.readlines()
                randNo = random.randint(0,2)
                questionsList = lines[randNo].split(', ')
                generator = 1
                print(questionsList)
        win = pygame.display.set_mode((800,600))
        
        qBoxWidth = 500
        qBoxLength = 50
        qBoxPosX = 50
        qboxPosy = 330
        pygame.draw.rect(win,(255,0,0), (qBoxPosX, qboxPosy, qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,0,0), (qBoxPosX, (qboxPosy + 100), qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,0,0), (qBoxPosX, (qboxPosy + 200), qBoxWidth, qBoxLength))
        font = pygame.font.Font('freesansbold.ttf', 32)
        win.blit(font.render(questionsList[0], True, (255,255,255)),(50,230))
        questionImg = pygame.transform.scale(pygame.image.load(filedir + '/pics/' + questionsList[5].rstrip('\n')), (269, 187))
        win.blit(questionImg,(50,25))
        if ' - right' in questionsList[1]:
                rightAnswer = questionsList[1].replace(" - right", "")
                win.blit(font.render(questionsList[1].replace(" - right", ""), True, (255,255,255)),(50,330))
                rightAnswerNo = 1
        else:
                win.blit(font.render(questionsList[1], True, (255,255,255)),(50,330))

        if ' - right' in questionsList[2]:
                rightAnswer = questionsList[2].replace(" - right", "")
                win.blit(font.render(questionsList[2].replace(" - right", ""), True, (255,255,255)),(50,430))
                rightAnswerNo = 2
        else:
                win.blit(font.render(questionsList[2], True, (255,255,255)),(50,430))
                
        if ' - right' in questionsList[3]:
                rightAnswer = questionsList[3].replace(" - right", "")
                win.blit(font.render(questionsList[3].replace(" - right", ""), True, (255,255,255)),(50,530))
                rightAnswerNo = 3
        else:
                win.blit(font.render(questionsList[3], True, (255,255,255)),(50,530))
                
        pygame.display.update()
        for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = event.pos
                    print(str(mousex) +','+ str(mousey))
                    print(game_status)  
                    if 500 > mousex > 50  and (qboxPosy + 50) > mousey > qboxPosy:
                        if rightAnswerNo == 1:
                                rightJingle.play(0)
                                ExamScore = ExamScore + int(questionsList[4])
                                generator = 0
                                game_status = 'Exam Question 5'
                        else:
                                wrongJingle.play(0)
                                generator = 0
                                game_status = 'Exam Question 5'
                                
                            
                    elif 500 > mousex > 50  and ((qboxPosy + 100) + 50) > mousey > (qboxPosy + 100):
                        if rightAnswerNo == 2:
                                rightJingle.play(0)
                                ExamScore = ExamScore + int(questionsList[4])
                                generator = 0
                                game_status = 'Exam Question 5'
                        else:
                                wrongJingle.play(0)
                                generator = 0
                                game_status = 'Exam Question 5'
                            
                    elif 500 > mousex > 50  and ((qboxPosy + 200) + 50) > mousey > (qboxPosy + 200):
                        if rightAnswerNo == 3:
                                rightJingle.play(0)
                                ExamScore = ExamScore + int(questionsList[4])
                                generator = 0
                                game_status = 'Exam Question 5'
                        else:
                                wrongJingle.play(0)
                                generator = 0
                                game_status = 'Exam Question 5'


while game_status == 'Exam Question 5':
        while generator != 1:
                script = open(filedir + '/script/Exam questions/' + game_status +'.txt', 'r')
                lines = script.readlines()
                randNo = random.randint(0,2)
                questionsList = lines[randNo].split(', ')
                generator = 1
                print(questionsList)
        win = pygame.display.set_mode((800,600))
        
        qBoxWidth = 500
        qBoxLength = 50
        qBoxPosX = 50
        qboxPosy = 330
        pygame.draw.rect(win,(255,0,0), (qBoxPosX, qboxPosy, qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,0,0), (qBoxPosX, (qboxPosy + 100), qBoxWidth, qBoxLength))
        pygame.draw.rect(win,(255,0,0), (qBoxPosX, (qboxPosy + 200), qBoxWidth, qBoxLength))
        font = pygame.font.Font('freesansbold.ttf', 32)
        win.blit(font.render(questionsList[0], True, (255,255,255)),(50,230))
        questionImg = pygame.transform.scale(pygame.image.load(filedir + '/pics/' + questionsList[5].rstrip('\n')), (269, 187))
        win.blit(questionImg,(50,25))
        if ' - right' in questionsList[1]:
                rightAnswer = questionsList[1].replace(" - right", "")
                win.blit(font.render(questionsList[1].replace(" - right", ""), True, (255,255,255)),(50,330))
                rightAnswerNo = 1
        else:
                win.blit(font.render(questionsList[1], True, (255,255,255)),(50,330))

        if ' - right' in questionsList[2]:
                rightAnswer = questionsList[2].replace(" - right", "")
                win.blit(font.render(questionsList[2].replace(" - right", ""), True, (255,255,255)),(50,430))
                rightAnswerNo = 2
        else:
                win.blit(font.render(questionsList[2], True, (255,255,255)),(50,430))
                
        if ' - right' in questionsList[3]:
                rightAnswer = questionsList[3].replace(" - right", "")
                win.blit(font.render(questionsList[3].replace(" - right", ""), True, (255,255,255)),(50,530))
                rightAnswerNo = 3
        else:
                win.blit(font.render(questionsList[3], True, (255,255,255)),(50,530))
                
        pygame.display.update()
        for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = event.pos
                    print(str(mousex) +','+ str(mousey))
                    print(game_status)  
                    if 500 > mousex > 50  and (qboxPosy + 50) > mousey > qboxPosy:
                        if rightAnswerNo == 1:
                                rightJingle.play(0)
                                ExamScore = ExamScore + int(questionsList[4])
                                game_status = 'End Exam'
                        else:
                                wrongJingle.play(0)
                                game_status = 'End Exam'
                                
                            
                    elif 500 > mousex > 50  and ((qboxPosy + 100) + 50) > mousey > (qboxPosy + 100):
                        if rightAnswerNo == 2:
                                rightJingle.play(0)
                                ExamScore = ExamScore + int(questionsList[4])
                                game_status = 'End Exam'
                        else:
                                wrongJingle.play(0)
                                game_status = 'End Exam'
                            
                    elif 500 > mousex > 50  and ((qboxPosy + 200) + 50) > mousey > (qboxPosy + 200):
                        if rightAnswerNo == 3:
                                rightJingle.play(0)
                                ExamScore = ExamScore + int(questionsList[4])
                                game_status = 'End Exam'
                        else:
                                wrongJingle.play(0)
                                game_status = 'End Exam'    
        

        
                

                            
                	
		
