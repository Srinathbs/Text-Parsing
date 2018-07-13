import sys


class TextParsing(object):
    """
    Text Parsing takes data from the input.txt file through pipe and
    Writes the output through pipe
    """

    def get_data(self):
        """
        The get data function reads the data sent as the argument and
        removes the additional empty lines present in the data
        Args:
                None
        Returns:
                input_data : list of lines
        """
        input_data = sys.stdin.readlines()
        input_data = [x for x in input_data if x != '\n']
        return input_data

    def number_parsing(self, index_list, line):
        """
        The number parsing function replaces the '*' bullet with the number
        index
        Args:
                index_list (list): list with the indexing depth and the index
                                    number
                line (string): line on which parsing is performed

        Returns:
                start_index (int): position from which next nested line should
                                    be written
        """
        index_count = len(line) - len(line.lstrip('*'))
        if index_count == len(index_list):
            index_list[-1] += 1
        elif index_count > len(index_list):

            for x in range((len(index_list)), index_count):
                index_list.append(1)

        elif index_count == 1:
            index_list[0] += 1
            index_list = index_list[:1]
        else:
            index_list = index_list[:index_count]
            index_list[-1] += 1
        out_str = ".".join([str(b) for b in index_list])
        start_index = len(out_str) + 2
        out_str = out_str + line.lstrip('*')
        print out_str,
        return start_index

    def bullet_parsing(self, start_index, line1, text, index):
        """
        The bullet parsing function replaces the '.' bullet with the nested
        format
        Args:
                start_index (int): position from which line should be written
                line1 (string) : line on which parsing is performed
                text (List): input data which is a list of strings
                index (int): starting position of the strings yet to be
                            processed
        Returns:
                start_index (int): position from which next nested line should
                                    be written
        """
        if text[index].startswith('*'):
            print '-'.rjust(start_index), line1.lstrip('.'),
            return start_index
        line1_index_count = len(line1) - len(line1.lstrip('.'))
        j = index
        while not text[j].startswith('.'):
            if j == len(text) - 1:
                print '-'.rjust(start_index), line1.lstrip('.'),
                print '-'.rjust(start_index - 1), text[j],
                exit(0)
            j += 1
        line2_index_count = len(text[j]) - len(text[j].lstrip('.'))
        if line1_index_count >= line2_index_count:

            print '-'.rjust(start_index), line1.lstrip('.'),
        else:
            print '+'.rjust(start_index), line1.lstrip('.'),
            start_index = start_index + 2

        return start_index

    def parse_text(self):
        """
        The parse text function performs the formatting of the data
        Args:
                None
        Returns:
                None
        """

        text = self.get_data()
        line1 = text[0]
        index_list = [0]
        start_index = 3
        for i in range(1, len(text)):

            if line1.startswith('*'):
                start_index = self.number_parsing(index_list, line1)
            elif line1.startswith('.'):
                start_index = self.bullet_parsing(start_index, line1, text, i)
            else:
                print "".rjust(start_index - 1), line1,
            line1 = text[i]
        # Parse the last line
        if text[-1].startswith('*'):
            self.number_parsing(index_list, text[-1])
        elif text[-1].startswith('.'):
            print '-'.rjust(start_index), text[-1].lstrip('.'),
        else:
            print "".rjust(start_index - 1), text[-1],


if __name__ == "__main__":
    parse = TextParsing()
    parse.parse_text()
