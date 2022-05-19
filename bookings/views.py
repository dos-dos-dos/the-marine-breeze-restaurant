from django.shortcuts import render
from tables.models import Tables


# Create your views here.
def make_booking_page(request):
    '''

    '''
    table_no = Tables.objects.all().get(id=int(request.GET['table_id']))
    return HttpResponse(render(request,'user/bookings.html',{'table_no':table_no}))

def book_table(request):
    '''

    '''    
    if request.method =="POST":

        table_id = request.POST['table_id']
        
        table_no = Tables.objects.all().get(id=table_id)
        #for finding the reserved rooms on this time period for excluding from the query set
        for each_booking in Bookings.objects.all().filter(booking_date = table_date):
            if str(each_booking.start_time) < str(request.POST['start_time']) and str(each_reservation.end_time) < str(request.POST['end_time']):
                pass
            elif str(each_booking.start_time) > str(request.POST['start_time']) and str(each_reservation.end_time) > str(request.POST['end_time']):
                pass
            else:
                messages.warning(request,"Sorry This Room is unavailable for Booking")
                return redirect("homepage")
            
        current_user = request.user
        total_person = int( request.POST['person'])
        booking_id = (table_no) + str(datetime.datetime.now())

        booking = Bookings()
        table_object = Tables.objects.all().get(id=table_id)
        table_object.status = '2'
        
        user_object = User.objects.all().get(username=current_user)

        booking.guest = user_object
        booking.table = table_object
        person = total_person
        booking.start_time = request.POST['start_time']
        booking.end_time = request.POST['end_time']

        booking.save()

        messages.success(request,"Congratulations! Booking Successfull")

        return redirect("homepage")
    else:
        return HttpResponse('Access Denied')

def handler404(request):
    return render(request, '404.html', status=404)