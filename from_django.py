def CreateJob(request):
    response_data = {}

    if request.method == 'POST':
        job_name = request.POST.get('job_name')
        try:
            name = Job.objects.get(name=job_name)
        except Job.DoesNotExist:
            return JsonResponse({'log': 'Job does not exist'})

        deadline = request.POST.get('job_deadline')
        parse_deadline = datetime.strptime(deadline, '%d-%m-%y').date()
        volume = request.POST.get('job_volume')
        stage_id = request.POST.get('job_stage')

        job_form = CreateJobForm({
            'name': name.id,
            'deadline': parse_deadline,
            'stage': stage_id,
            'volume': volume
        })
        if job_form.is_valid():
            job_form.save()
            response_data['log'] = 'form valid and saved'
            response_data['name'] = name.name
            response_data['volume'] = volume
            response_data['deadline'] = parse_deadline
            response_data['price'] = name.price
        else:
            response_data['log'] = 'form is not valid!'

        return JsonResponse(response_data)

    else:
        return JsonResponse({'log': 'no data'})


def ChangeStatus(request):
    response_data = {}

    if request.method == "POST":
        job_id = request.POST.get('job_id')
        try:
            job = Jobs.objects.get(id=job_id)
        except Job.DoesNotExist:
            return JsonResponse({'log': 'Job does not exist'})

        if job.status == 0:
            job.status = 1
            response_data['old_status'] = 'all_good'
            response_data['new_status'] = 'td-warning'
        else:
            job.status = 0
            response_data['old_status'] = 'td-warning'
            response_data['new_status'] = 'all_good'

        job.save()
        response_data['log'] = 'Status changed!'

    else:
        response_data['log'] = 'Something error!'

    return JsonResponse(response_data)


def ChangeStatus(request):
    response_data = {}

    if request.method == "POST":
        job_id = request.POST.get('job_id')
        try:
            job = Jobs.objects.get(id=job_id)
        except Job.DoesNotExist:
            return JsonResponse({'log': 'Job does not exist'})

        if job.status == 0:
            job.status = 1
            response_data['old_status'] = 'all_good'
            response_data['new_status'] = 'td-warning'
        else:
            job.status = 0
            response_data['old_status'] = 'td-warning'
            response_data['new_status'] = 'all_good'

        job.save()
        response_data['log'] = 'Status changed!'

    else:
        response_data['log'] = 'Something error!'

    return JsonResponse(response_data)
