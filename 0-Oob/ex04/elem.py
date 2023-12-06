#!/usr/bin/python3

import traceback
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
        if (type(content) == str and content == ''):
            raise Elem.ValidationError
        self.tag = tag
        self.attr = dict(attr)
        ret = str()
        if(type(content) == list ):
            for c in list(content):
                if (str(c) == ''): continue
                ret += '\n  ' +  str(c)
            if (ret):
                ret += '\n'
        elif (type(content) == Elem):
            ret = '\n'
            for c in str(content).split('\n'):
                ret += '  ' + str(c) + "\n"

        elif(content):
            ret = "\n  " + str(content) + "\n"
        self.content = ret
        self.tag_type = tag_type
        if(self.tag_type != 'double' and self.tag_type != 'simple'):
            raise Elem.ValidationError

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        if self.tag_type == 'double':
            if (self.attr != {}):
                result = f"<{self.tag} {self.attr}>{self.content}</{self.tag}>"
            else:
                result = f"<{self.tag}>{self.content}</{self.tag}>"
        elif self.tag_type == 'simple':
            if (self.attr != {}):
                result = f"<{self.tag} {self.attr}>{self.content}"
            else:
                result = f"<{self.tag}>{self.content}"
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
    try:
        html = Elem(tag="html", content=[
            Elem(tag="head", content=Elem(tag="title", content=Text("Hello ground!"))),
            Elem(tag="body", content=[
                Elem(tag="h1", content=Text("Hgit o no, not again!")),
                Elem(tag="img", attr={"src": "http://i.imgur.com/pfp3T.jpg"}, tag_type='simple'),
            ])
        ])
    except AssertionError as e:
        print ('\033[91m')
        traceback.print_exc()
        print(e)
        print('Tests failed!')
    print (html)
