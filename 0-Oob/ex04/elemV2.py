#!/usr/bin/python3

"""
    WIP
"""

class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        return super().__str__().replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace('\n', '\n<br />\n')


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    class ValidationError(Exception):
        def __init__(self, *args: object) -> None:
            super().__init__(*args)


    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        if (not self.check_type(content) and content != None):
            raise Elem.ValidationError
        if(tag_type != 'double' and tag_type != 'simple'):
            raise Elem.ValidationError
        self.tag = tag
        self.attr = dict(attr)
        if (type(content) != list and content    != None):
            content = [content]
        self.content = content if content != [] else Text('')
        print (f"\033[91m {type(self.content)}\033[00m")
        self.tag_type = tag_type

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        if self.tag_type == 'double':
            if (self.attr != {}):
                result = f"<{self.tag}{self.__make_attr()}>{self.__make_content()}</{self.tag}>"
            else:
                result = f"<{self.tag}>{self.__make_content()}</{self.tag}>"
        elif self.tag_type == 'simple':
            if (self.attr != {}):
                result = f"<{self.tag}{self.__make_attr()} />"
            else:
                result = f"<{self.tag} />"
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            result += str(elem)
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


if __name__ == '__main__':

    # html = Elem(tag="html", content=[
    #     Elem(tag="head", content=Elem(tag="title", content=Text("Hello ground!"))),
    #     Elem(tag="body", content=[
    #         Elem(tag="h1", content=Text("Hgit o no, not again!")),
    #         Elem(tag="img", attr={"src": "http://i.imgur.com/pfp3T.jpg"}, tag_type='simple'),
    #     ])
    # ])

    html = Elem("")

    # html = Elem(tag="html", content=[
    #     Elem(tag='head', content="je suis la head"),
    #     Elem(tag='body'),
    # ])
    print (html)
