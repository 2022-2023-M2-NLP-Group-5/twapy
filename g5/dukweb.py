#!/usr/bin/env python3

import sys
import fire
# import csvkit

# appears to be 100 values in vectors in DUKweb word2vec CSVs (+1 label at left-hand side)
EXPECTED_NUM_OF_COLUMNS = 101

# from 2001.csv, line 404147.
TEST_INPUT_CSV_LINE_101 = 'mrchad,-0.09788409,0.4799716,0.046219707,0.1546636,-0.14432976,-0.8346738,0.40899593,-0.13525106,-0.061364938,0.25927752,0.11140222,0.17873521,0.44135502,-0.6661329,0.3751186,0.40065968,-0.22055155,0.120848544,-0.39443743,-0.337011,-0.050851848,1.1650224,0.029696044,0.34967166,-0.27739182,0.23129922,0.5458337,0.21658395,0.2639568,-0.12796938,-0.28940076,-0.024023548,0.28638154,-0.20788607,-0.045535095,0.2578506,0.14573407,-0.056690153,-0.06721537,-0.36051238,-0.2759409,-0.08510435,0.20202637,-0.16493554,-0.26227462,0.6480989,0.20306517,-0.27746844,0.47140607,-0.09999756,-0.027160123,-0.22270174,0.07197737,0.45394328,-0.02452308,-0.31284624,-0.2605321,0.51039517,0.06562866,0.2512263,0.33999482,-0.074608654,-0.2869339,0.02865802,0.3727891,-0.42468905,-0.071007185,0.016423333,-0.15690573,-0.23019901,-0.13056216,0.09462869,-0.4499953,0.3802745,0.4494455,-0.18893015,-0.6941543,0.4728387,0.590737,0.06787326,0.09068346,0.11476699,-0.16045089,-0.04128004,0.34516722,0.009461783,0.05705553,-0.26916263,-0.48747477,-0.4069507,-0.29812297,-0.0022345055,0.56762815,0.031289812,0.46638936,-0.2563091,0.2576961,-0.09147122,0.12327548,-0.032341335'

# from 2001.csv, line 403560.
TEST_INPUT_CSV_LINE = '0,45,200,75,0.6959519,0.15556665,-2.1345785,0.64726514,-0.040464535,-0.041206643,0.44315243,0.998356,0.7949734,0.56542236,-0.14790657,0.24554877,-0.461942,-0.60847574,0.92653114,-1.1931028,-0.33425114,-1.9357481,0.4881968,-1.1136767,-0.9594933,-0.6475114,0.25085753,-2.4733949,-0.17515688,-1.4320831,-0.21458192,-0.6513927,-1.2567055,-0.08920267,0.0030699673,-1.1459905,1.9278104,-0.24598223,0.41016117,0.26231253,0.18498933,0.9823095,0.13948044,-0.703723,0.80187154,0.024371592,-0.25990137,1.0983909,0.92962825,-0.54152405,-0.10621621,0.89965785,1.7742996,-0.060763218,-0.14115164,0.74272877,0.34658033,1.2109945,0.40582383,-1.3044001,0.65597653,0.43522844,0.38830674,0.20941672,-0.15420924,-0.31076598,0.8081266,0.1755396,0.7903163,-0.4942455,-0.5863973,0.6989076,-0.653118,-0.6761732,0.09957233,0.2512681,-1.247306,0.70148385,1.2599863,-0.20120129,0.99778616,-1.1003504,-0.7290651,-0.0993824,-0.10911099,0.2881713,-0.07595195,0.037148193,1.1413398,1.5048574,0.4969082,0.31531206,-1.3281054,-0.1282433,0.65913856,0.24553142,-0.66576135,-0.56657374,0.7032474,1.1736007,0.28181347,1.3322632,-0.51723164,0.8689958'

def sniff_proper_number_of_columns(filepath):
    # get the mode average of the number of fields
    pass

def normalize_csv_line_merge_left(input_line:str, n_output_cols:int) -> str:
    # segmentation could be more robust but probably not needed for DUKweb csv
    # files
    orig_fields = input_line.strip('\n').split(',')

    if len(orig_fields) < n_output_cols:
        raise Exception('line has fewer orig_fields than expected output columns')
    split_before_index = len(orig_fields) - n_output_cols + 1

    right_part = orig_fields[split_before_index:]
    left_part = orig_fields[:split_before_index]

    left_part_merged = '\"' + ','.join(left_part) + '\"'

    out_fields = [left_part_merged] + right_part
    output_line = ','.join(out_fields)

    merge_happened_msg = ''
    if len(orig_fields) != n_output_cols:
        merge_happened_msg = '*MERGE HAPPENED*'

    print('{} orig fields, {} output fields, split index: {}  {} :: {}'.
          format(len(orig_fields), n_output_cols, split_before_index,
                 merge_happened_msg, left_part_merged),
          file=sys.stderr)

    # print(output_line, file=sys.stderr)
    return output_line

def normalize_lines(infilepath, columns):
    """generator"""
    with open(infilepath, 'r') as infile:
        for line_num, line in enumerate(infile):
            print('line #: {}'.format(line_num), file=sys.stderr)
            output_line = normalize_csv_line_merge_left(line, columns)
            yield output_line

def normalize_csv_columns(infilepath, columns:int=EXPECTED_NUM_OF_COLUMNS, outfilepath=None):
    if outfilepath == None:
        outfilepath = sys.stdout

    for l in normalize_lines(infilepath, columns):
        print(l, file=outfilepath)

if __name__ == '__main__':
    # normalize_csv_line_merge_left(TEST_INPUT_CSV_LINE, EXPECTED_NUM_OF_COLUMNS)
    fire.Fire()
