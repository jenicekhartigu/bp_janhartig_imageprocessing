# -*- coding: utf-8 -*-

import sys
import argparse

import functions

def parse_args(args):
    """
    Naparsování argumentu
    """
    parser = argparse.ArgumentParser(description=
                'Tento program je pro otestování jednotlivých funkcí z OpenCV.'
                'Popis funkcí programu')
    parser.add_argument("-i", "--input",
                        help="Nazev vstupniho souboru")
    #parser.add_argument("-l", "--list",
    #                    help="Soubor se slovy k cenzuře.",
    #                    default=None)
    parser.add_argument("-trans", "--transformation",
                        help="Transformace obrazu",
                        action='store_true',
                        default=False)
    parser.add_argument("-red", "--red_part",
                        help="Zobrazení červeného spektra",
                        action='store_true',
                        default=False)
    parser.add_argument("-noise", "--noise_reduction",
                        help="Odstraneni šumu z obrazku",
                        action='store_true',
                        default=False)
    parser.add_argument("-eros", "--erosion",
                        help="Eroze",
                        action='store_true',
                        default=False)
    parser.add_argument("-dilate", "--dilatation",
                        help="Dilatace",
                        action='store_true',
                        default=False)
    parser.add_argument("-edge", "--findEdges",
                        help="Find edges of object on picture",
                        action='store_true',
                        default=False)
    args = parser.parse_args(args)
    if args.input is None:
        parser.error("Vyberte jednu z funkcí")
    return {'file': args.input,
            'red_part': args.red_part,
            'transformation': args.transformation,
            'noise': args.noise_reduction,
            'eros': args.erosion,
            'dilate': args.dilatation,
            'edge': args.findEdges}
    #return { 'list': args.list, 'red_part': args.output,
    #        'transformation': args.clean}

def main():
    arguments = parse_args(sys.argv[1:])
    file = arguments['file']
    if arguments['transformation']:
        functions.nacti_display(file)
    if arguments['red_part']:
        functions.read_jpg_to_red(file)
    if arguments['noise']:
        functions.remove_noise(file)
    if arguments['eros']:
        functions.erosion(file)
    if arguments['dilate']:
        functions.dilatation(file)
    if arguments['edge']:
        functions.edges(file)
    #else:
    #    cv2.imshow('file', file)
    

if __name__ == '__main__':
   main()