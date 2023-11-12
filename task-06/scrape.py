import requests, bs4, re,csv 
def html_remove(data):
    pat = re.compile(r'<.*?>')
    return pat.sub('', data)

def live_scrape():
    res= requests.get('https://www.espncricinfo.com/live-cricket-score')

    text= bs4.BeautifulSoup(res.text,'html.parser')

    team_1=[]

    team_2 = []

    score_list=[]

    current_state=[]

    team_scrape_html = text.select('p')


    score_scrape_html = text.select('strong')

    lenght = len(team_scrape_html)

    for i in range(lenght):
        if i % 3 == 0:
            team_1.append(html_remove(str(team_scrape_html[i])))
        elif i % 3 == 1:
            team_2.append(html_remove(str(team_scrape_html[i])))
        else:
            current_state.append(html_remove(str(team_scrape_html[i])))

            k=0

    lenght_2=len(score_scrape_html)

    for j in range(lenght_2):
        score_list.append(html_remove(str(score_scrape_html[j])))

    k=0 

    lenght=len(team_1)
    limit= len(score_list)

    try:
        for m in range(1):
            if current_state[m]=='Match yet to begin':
                return(f'{team_1[m]}(0/0) vs {team_2[m]}(0/0)\n{current_state[m]}')
            elif current_state[m].lower()=='null':
                return(f'{team_1[m]} vs {team_2[m]}\n{"Not covered live"}')
            elif 'chose' in current_state[m].lower():
                if k+1<limit:
                    k+=1
                return(f'{team_1[m]}({score_list[k]}) vs {team_2[m]}(0/0)\n{current_state[m]}')
            
            else:
                if (k+3<limit and (current_state[m]!='Match yet to begin')) and (k+3<limit and 'chose' not in current_state[m]) and (k+3<limit and (current_state[m].lower()!='null')) :
                    k+=2
                return(f'{team_1[m]}({score_list[k]}) vs {team_2[m]}({score_list[k+1]})\n{current_state[m]}')


    except IndexError:
        pass
    


def csv_scrape():

    res= requests.get('https://www.espncricinfo.com/live-cricket-score')

    text= bs4.BeautifulSoup(res.text,'html.parser')

    team_1=[]

    team_2 = []

    score_list=[]

    current_state=[]

    team_scrape_html = text.select('p')


    score_scrape_html = text.select('strong')

    lenght = len(team_scrape_html)

    for i in range(lenght):
        if i % 3 == 0:
            team_1.append(html_remove(str(team_scrape_html[i])))
        elif i % 3 == 1:
            team_2.append(html_remove(str(team_scrape_html[i])))
        else:
            current_state.append(html_remove(str(team_scrape_html[i])))

            k=0

    lenght_2=len(score_scrape_html)

    for j in range(lenght_2):
        score_list.append(html_remove(str(score_scrape_html[j])))

    k=0 

    lenght=len(team_1)
    limit= len(score_list)

    try:
        with open('cricket_scores.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            for m in range(lenght):
                if current_state[m]=='Match yet to begin':
                    csvwriter.writerow([f'{team_1[m]}(0/0) vs {team_2[m]}(0/0)', current_state[m]])
                elif current_state[m].lower()=='null':
                    csvwriter.writerow([f'{team_1[m]} vs {team_2[m]}', "Not covered live"])
                elif 'chose' in current_state[m].lower():
                    csvwriter.writerow(f'{team_1[m]}({score_list[k]}) vs {team_2[m]}(0/0)', current_state[m])
                    if k+1<limit:
                        k+=1
                else:
                    csvwriter.writerow(f'{team_1[m]}({score_list[k]}) vs {team_2[m]}({score_list[k+1]})\n{current_state[m]}')

                    if (k+3<limit and (current_state[m]!='Match yet to begin')) and (k+3<limit and 'chose' not in current_state[m]) and (k+3<limit and (current_state[m].lower()!='null')) :
                        k+=2
            print("Done")
    except IndexError:
        pass

csv_scrape()