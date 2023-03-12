class Page:
    def __int__(self):
        self.url = 'www.amazon.com'

    def open_url(self):
        print('Url opening', self.url)

    def close(self):
        print('Closing the page', self.url)


p = Page()

p.open_url()