from pathlib import Path
import json
root=Path(__file__).resolve().parent
# Values transcribed from the saved notebook outputs, not recomputed by fitting models.
data={
 'source':'ml_course_mai/lab02/lab02_solution.ipynb',
 'counts':{'all':891,'dead':549,'survived':342,'train':712,'test':179,'trainDead':439,'trainSurvived':273,'testDead':110,'testSurvived':69},
 'splitRounded':{'train':[.617,.383],'test':[.615,.385]},
 'medianAge':28.5,
 'features':['Age','SibSp','Parch','Fare','Pclass','Sex','Embarked'],
 'columns':['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked'],
 'models':[
 {'name':'Baseline','cv':0,'std':0,'test':0,'train':0,'metrics':[.615,0,0,0],'cm':[110,0,69,0]},
 {'name':'Decision Tree','cv':.721,'std':.013,'test':.682,'train':.802,'metrics':[.771,.733,.638,.682],'cm':[94,16,25,44]},
 {'name':'Random Forest','cv':.741,'std':.040,'test':.715,'train':.879,'metrics':[.804,.815,.638,.715],'cm':[100,10,25,44]},
 {'name':'Gradient Boosting','cv':.753,'std':.031,'test':.704,'train':.865,'metrics':[.793,.786,.638,.704],'cm':[98,12,25,44]},
 {'name':'SVM','cv':.745,'std':.031,'test':.736,'train':.779,'metrics':[.816,.821,.667,.736],'cm':[100,10,23,46]},
 {'name':'KNN','cv':.718,'std':.016,'test':.750,'train':.798,'metrics':[.821,.814,.696,.750],'cm':[99,11,21,48]}],
 'eda':[
 {'title':'Пол','labels':['Женщины','Мужчины'],'values':[.743,.185],'n':[253,459],'note':'Женщины выживали чаще мужчин.'},
 {'title':'Класс билета','labels':['Первый','Второй','Третий'],'values':[.649,.447,.243],'n':[171,150,391],'note':'Первый класс — выше третьего по выживаемости.'},
 {'title':'Возраст','labels':['≤ 12 лет','12–18','18–40','40–60','> 60 лет'],'values':[.600,.415,.382,.410,.188],'n':[55,53,346,105,16],'note':'Дети до 12 лет выживали чаще взрослых 18–40 лет.'}],
 'importance':{
 'Decision Tree':{'Sex':.548,'Fare':.121,'Age':.103,'Pclass':.191,'Embarked':.035,'SibSp':.002,'Parch':.001},
 'Random Forest':{'Sex':.372,'Fare':.211,'Age':.184,'Pclass':.126,'Embarked':.040,'SibSp':.037,'Parch':.031},
 'Gradient Boosting':{'Sex':.466,'Fare':.178,'Age':.150,'Pclass':.153,'Embarked':.022,'SibSp':.028,'Parch':.002}},
 'errors':[
 {'title':'Пол','labels':['Женщины','Мужчины'],'n':[61,118],'errors':[13,24],'rate':[.213,.203]},
 {'title':'Класс билета','labels':['Первый','Второй','Третий'],'n':[45,34,100],'errors':[12,4,21],'rate':[.267,.118,.210]},
 {'title':'Возраст','labels':['≤ 12 лет','12–18','18–40','40–60','> 60 лет','Неизвестен'],'n':[14,17,79,23,6,40],'errors':[4,1,16,5,1,10],'rate':[.286,.059,.203,.217,.167,.250]}],
 'examples':[{'id':18,'sex':'мужчина','pclass':2,'age':'неизвестен','fare':'13','pred':0,'true':1,'note':'Гипотеза: модель опиралась на низкую выживаемость мужчин.'},{'id':200,'sex':'женщина','pclass':2,'age':'24 года','fare':'13','pred':1,'true':0,'note':'Гипотеза: высокая выживаемость женщин повлияла на прогноз.'}]
}
(root/'data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
html=(root/'template.html').read_text()
(root/'index.html').write_text(html.replace('/*__DATA__*/',json.dumps(data,ensure_ascii=False)),encoding='utf-8')
print(root/'index.html')
