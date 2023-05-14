def salesRegister(request):
    p_total = 0
    c_total = 0
    s_total = 0
    p_total_amt = 0
    lst2 = []
    lst1 = []
    pat_info = Patient_info.objects.all()
    recor = None
    recor = Payment_info.objects.all()

 
    if request.method == 'POST':
        startdate = request.POST['fdate']
        enddate = request.POST['tdate']

        cus = Patient_info.objects.all()
        for i in cus:
            lst = []
            records = Payment_info.objects.filter(patient_id = i.id, time_stamp__date__range=(startdate, enddate))
            p_total = 0
            c_total = 0
            s_total = 0
            p_total_amt = 0
            for p in records:
                c_total = c_total + p.c_gst
                s_total = s_total + p.s_gst
                p_total_amt = p_total_amt + p.total_amount
                p_total = p_total + p.amount

            lst.append(p.patient_id.id)
            lst.append(p_total)
            lst.append(p_total_amt)
            lst.append(s_total)
            lst.append(c_total)
            lst2.append(lst)
            lst1.append(p.patient_id.id)
        print(lst2)

    return render(request, 'recors.html', {'lst2':lst2, 'record':recor, 'pat':pat_info, 'p_lst':lst1})












dict1 = {'ID': {'Name':'Shivu', 'Place':'Hosadurga', 'Total':89000, 'Total_amt': 45000, 'C_gst': 3400, 'S_gst': 3400},
             'ID1': {'Name':'Shivu', 'Place':'Hosadurga', 'Total':89000, 'Total_amt': 45000, 'C_gst': 3400, 'S_gst': 3400}}
    print(dict1['ID'])
    for value in dict1['ID'].items():