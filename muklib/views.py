from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt


def intro(request):
    request.session['visit_intro'] = True
    return render(request, 'intro.html')


def action(request):
    visit_intro = request.session.get('visit_intro', False)
    if not visit_intro:
        return redirect('intro')

    from muklib.data import BIG_CLASS, SMALL_CLASS
    template_data = {'big': BIG_CLASS, 'small': SMALL_CLASS}

    return render(request, 'action.html', template_data)


@csrf_exempt
def result(request):
    if request.method == 'GET':
        return redirect('action')

    try:
        action_type = request.POST['type']
        action_data = request.POST['data'].split(',')
    except MultiValueDictKeyError:
        return redirect('action')

    if action_type == 'big':
        from muklib.data import BIG_CLASS
        result_data = list(BIG_CLASS)
    elif action_type == 'small':
        from muklib.data import SMALL_CLASS
        result_data = list(SMALL_CLASS)
    else:
        return redirect('action')

    for data in action_data:
        if not data in result_data:
            return redirect('action')
        result_data.remove(data)

    return render(request, 'result.html', {'result': result_data})