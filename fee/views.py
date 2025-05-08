from django.shortcuts import render

def fees_view(request):
    fees_data = [
        {'course': 'MCA', 'duration': '2 Years', 'amount': '₹1,20,000/year'},
        {'course': 'BCA', 'duration': '3 Years', 'amount': '₹1,00,000/year'},
    ]
    return render(request, 'fees.html', {'fees': fees_data})
