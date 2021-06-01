from flask import Flask,render_template
import requests

app=Flask(__name__)

@app.route("/")
def home():
    url="https://api.covid19india.org/state_district_wise.json"
    url2="https://api.covid19india.org/data.json"
    r=requests.get(url).json()
    r2=requests.get(url2).json()
    print(r2['statewise'][17])
    district=["Alappuzha","Ernakulam","Idukki","Kannur","Kasaragod","Kollam","Kottayam","Kozhikode","Malappuram","Palakkad","Pathanamthitta","Thiruvananthapuram","Thrissur","Wayanad"]
    delt=[]
    for i in district:
        d1=r["Kerala"]["districtData"][i]["delta"]["confirmed"]
        d2=r["Kerala"]["districtData"][i]["delta"]["deceased"]
        d3=r["Kerala"]["districtData"][i]["delta"]["recovered"]
        delt.append(d1)
        delt.append(d2)
        delt.append(d2)
    print(delt)
    cases={
     'Time':r2['statewise'][17]['lastupdatedtime'],
     'Total_a':r2['statewise'][17]['active'],
     'Delta_a':r2['statewise'][17]['deltaconfirmed'],
     'Total_d':r2['statewise'][17]['deaths'],
     'Delta_d':r2['statewise'][17]['deltadeaths'],
     'Total_r':r2['statewise'][17]['recovered'],
     'Delta_r':r2['statewise'][17]['deltarecovered'],
     'Al_active':r["Kerala"]["districtData"]["Alappuzha"]["active"],
     'Al_death':r["Kerala"]["districtData"]["Alappuzha"]["deceased"],
     'Al_recover':r["Kerala"]["districtData"]["Alappuzha"]["recovered"],
     'Er_active':r["Kerala"]["districtData"]["Ernakulam"]["active"],
     'Er_death':r["Kerala"]["districtData"]["Ernakulam"]["deceased"],
     'Er_recover':r["Kerala"]["districtData"]["Ernakulam"]["recovered"],
     'Id_active':r["Kerala"]["districtData"]["Idukki"]["active"],
     'Id_death':r["Kerala"]["districtData"]["Idukki"]["deceased"],
     'Id_recover':r["Kerala"]["districtData"]["Idukki"]["recovered"],
     'Ka_active':r["Kerala"]["districtData"]["Kannur"]["active"],
     'Ka_death':r["Kerala"]["districtData"]["Kannur"]["deceased"],
     'Ka_recover':r["Kerala"]["districtData"]["Kannur"]["recovered"],
     'Kas_active':r["Kerala"]["districtData"]["Kasaragod"]["active"],
     'Kas_death':r["Kerala"]["districtData"]["Kasaragod"]["deceased"],
     'Kas_recover':r["Kerala"]["districtData"]["Kasaragod"]["recovered"],
     'Ko_active':r["Kerala"]["districtData"]["Kollam"]["active"],
     'Ko_death':r["Kerala"]["districtData"]["Kollam"]["deceased"],
     'Ko_recover':r["Kerala"]["districtData"]["Kollam"]["recovered"],
     'Kot_active':r["Kerala"]["districtData"]["Kottayam"]["active"],
     'Kot_death':r["Kerala"]["districtData"]["Kottayam"]["deceased"],
     'Kot_recover':r["Kerala"]["districtData"]["Kottayam"]["recovered"],
     'Koz_active':r["Kerala"]["districtData"]["Kozhikode"]["active"],
     'Koz_death':r["Kerala"]["districtData"]["Kozhikode"]["deceased"],
     'Koz_recover':r["Kerala"]["districtData"]["Kozhikode"]["recovered"],
     'Ma_active':r["Kerala"]["districtData"]["Malappuram"]["active"],
     'Ma_death':r["Kerala"]["districtData"]["Malappuram"]["deceased"],
     'Ma_recover':r["Kerala"]["districtData"]["Malappuram"]["recovered"],
     'Pa_active':r["Kerala"]["districtData"]["Palakkad"]["active"],
     'Pa_death':r["Kerala"]["districtData"]["Palakkad"]["deceased"],
     'Pa_recover':r["Kerala"]["districtData"]["Palakkad"]["recovered"],
     'Pat_active':r["Kerala"]["districtData"]["Pathanamthitta"]["active"],
     'Pat_death':r["Kerala"]["districtData"]["Pathanamthitta"]["deceased"],
     'Pat_recover':r["Kerala"]["districtData"]["Pathanamthitta"]["recovered"],
     'Th_active':r["Kerala"]["districtData"]["Thiruvananthapuram"]["active"],
     'Th_death':r["Kerala"]["districtData"]["Thiruvananthapuram"]["deceased"],
     'Th_recover':r["Kerala"]["districtData"]["Thiruvananthapuram"]["recovered"],
     'Thr_active':r["Kerala"]["districtData"]["Thrissur"]["active"],
     'Thr_death':r["Kerala"]["districtData"]["Thrissur"]["deceased"],
     'Thr_recover':r["Kerala"]["districtData"]["Thrissur"]["recovered"],
     'Wa_active':r["Kerala"]["districtData"]["Wayanad"]["active"],
     'Wa_death':r["Kerala"]["districtData"]["Wayanad"]["deceased"],
     'Wa_recover':r["Kerala"]["districtData"]["Wayanad"]["recovered"],
      'delt':delt
    }
    
    return render_template("index.html",cases=cases)


if app == "__main__":
    app.run(debug=True)