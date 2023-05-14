from .models import Patient_info, Payment_info

t_sgst = []
t_cgst = []
t_total = []
t_amount = []
p_lst = []
def CreateList(value):
    p_lst=[]
    for i in value:
        p_lst.append(i.patient_id.id)

    new_list = list(set(p_lst)) 
    return new_list


def G_Total(value):
    t_sgst = []
    t_cgst = []
    t_total = []
    t_amount = []

    g_total = []

    for i in value:
        t_sgst.append(i.s_gst)
        t_cgst.append(i.c_gst)
        t_total.append(i.total_amount)
        t_amount.append(i.amount)

    g_total.append(sum(t_amount))
    g_total.append(sum(t_total))
    g_total.append(sum(t_sgst))
    g_total.append(sum(t_cgst))
    
    return g_total


def Total(value, start_date, end_date):
    sgst = 0
    cgst = 0
    t_total = 0
    t_amount = 0
    p_lst=[]
    t_lst = []
    lst = []
    for i in value:
        p_lst.append(i.patient_id.id)

    new_list = list(set(p_lst)) 
    print(new_list)

    for i in new_list:
        print(i)
        rec = Payment_info.objects.filter(patient_id = i, time_stamp__date__range=(start_date, end_date))
        print(rec)
        sgst = 0
        cgst = 0
        t_total = 0
        t_amount = 0
        lst = []
        for s in rec:
            sgst = sgst + s.c_gst
            cgst = cgst + s.s_gst
            t_total = t_total + s.total_amount
            t_amount = t_amount + s.amount

        lst.append(i)
        lst.append(t_amount)
        lst.append(t_total)
        lst.append(sgst)
        lst.append(cgst)

        t_lst.append(lst)
    print(t_lst)
    return t_lst
    


def Check(value):
    j = value.upper()
    try:
        if Patient_info.objects.get(patient_gst_no = j):
            return False
    except:
        return True


