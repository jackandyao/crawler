import math

class Page(object):

    def __init__(self, paginator, page_number=1, skip=0):
        self.page_number = page_number

        self.skip = skip

        self.paginator = paginator

        self.next_page_number = self.page_number + 1

        self.prev_page_number = self.page_number - 1

    def has_next(self):
        return self.page_number < self.paginator.total_records / float(self.paginator.per_page)

    def has_prev(self):
        return self.page_number > 1

    def get_next_page(self):
        return self.paginator.get_page(self.next_page_number)

    def get_prev_page(self):
        return self.paginator.get_page(self.prev_page_number)

#分页封装容器
class Paginator(object):
    def __init__(self, total_records=None, per_page=None):

        # total records
        self.total_records = total_records

        # perpage size
        self.per_page = per_page

        # total pages
        self.total_pages = 0

        # perpage skip infor
        self.data = {}

        self.__judge__()

    def __judge__(self):
        # caculate total pages
        if self.total_records > self.per_page:
            self.total_pages = int(math.floor(self.total_records / float(self.per_page)))

            self.data[1] = Page(self, page_number=1, skip=0)

            for i in range(1, self.total_pages):
                self.data[i + 1] = Page(self, page_number=i + 1, skip=self.data[i].skip + self.per_page)

                # 如果计算出来的页数不恰巧是个整数，那么还需要计算最后一页
            if self.total_pages < (self.total_records / float(self.per_page)):
                # 计算最后一页,因为最后一页肯定是能全页显示的
                self.data[self.total_pages + 1] = Page(self, self.total_pages + 1,
                                                       skip=self.data[self.total_pages].skip + self.per_page)
        else:
            self.total_pages = 1
            self.data[1] = Page(self, 1, skip=0)

    # def get_page(self, page_number):
    #     page_number = int(page_number)
    #     if page_number in self.data.keys():
    #         return self.data[page_number]
    #     else:
    #         return None


