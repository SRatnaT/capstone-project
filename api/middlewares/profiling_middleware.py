import cProfile
import io
import pstats
import time


class CProfileMiddleware:

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):

        profiler = cProfile.Profile()
        profiler.enable()

        start = time.time()

        response = self.get_response(request)

        duration = time.time() - start

        profiler.disable()

        # Creating temp storage to store the profiling stats

        temp_store = io.StringIO()
        stats = pstats.Stats(profiler, stream=temp_store).sort_stats("cumtime")
        stats.print_stats(50)

        print(f"\n--- PROFILE for {request.path}: {duration}")
        print(temp_store.getvalue())

        return response
