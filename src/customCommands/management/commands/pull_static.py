from django.core.management.base import BaseCommand
from django.conf import settings
import utilities

STATICFILES_VENDOR_DIR = getattr(settings, 'STATICFILES_VENDOR_DIR')


STATICFILES_URLS = {
    "flowbite.min.js":"https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js",
    "flowbite.min.css":"https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js.map":"https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js.map",
}

class Command(BaseCommand):
    help = "pull the static files from a URL in production mode"
    def handle(self, *args, **options):
        self.stdout.write("start downloading the static files")
        success_download_urls = []

        for name, url in STATICFILES_URLS.items():
            file_path = STATICFILES_VENDOR_DIR / name
            is_success = utilities.download_file(url, file_path)
            
            if is_success:
                success_download_urls.append(url)
            else:
                self.stdout.write(self.style.ERROR(f"failed downloading {url}"))
            
        if set(success_download_urls) == set(STATICFILES_URLS.values()):
            self.stdout.write(self.style.SUCCESS('updating the static files successfully'))
        else:
            self.stdout.write(self.style.WARNING('some files were not updated, try again'))

        