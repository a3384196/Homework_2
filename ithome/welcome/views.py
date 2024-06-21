from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
import numpy as np
import io
# Create your views here.
def index(request):
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.title('Sinewave Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()  # Close the figure to free up memory
    buffer.seek(0)

    return HttpResponse(buffer, content_type='image/png')