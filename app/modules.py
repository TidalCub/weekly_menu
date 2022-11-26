import datetime


def current_week_number():
    return datetime.datetime.now().isocalendar()[1]

def week_number(date):
    return datetime.datetime.strptime(date, "%d/%m/%Y").isocalendar()[1]

def menu_query_formate(query):
    for i in range(len(query)):

        return None

def menu_planner_url_format(menu_id):
    week_num = current_week_number()
    redirect_url = f"/menu/menu-planner?menuid={menu_id}&wdc={week_num}"
    return redirect_url

def dish_format(result):
    dishes = []
    for i in range(len(result)):
        tmp = []
        tmp.append(result[i].ID)
        tmp.append(result[i].DishName)
        tmp.append(result[i].Menu)
        tmp.append(result[i].Date)
        dishes.append(tmp)
    return dishes

def order_query_by_date(result):
    ordered = sorted(result, key=lambda x: x[3])
    return ordered

def show_current_weeks_dishes(data):
    for i in range(len(data)):
        
        print(week_number(data[i][3]))
    #return current_dishes