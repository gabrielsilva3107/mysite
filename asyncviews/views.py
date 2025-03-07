from django.http import HttpResponse
import asyncio

async def async_counter_view(request):
    for num in range(1, 11):
        print(num)
        await asyncio.sleep(1)  # Aguarda 1 segundo entre cada número

    return HttpResponse("Contador assíncrono finalizado!")
