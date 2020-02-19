#!/usr/bin/env python
# coding=utf-8

def parsefile(filename):
    ny_total = 0
    ny_avg = 0
    ny_con = 0

    sf_total = 0
    sf_avg = 0
    sf_con = 0

    for line in open(filename):
        if line.find("New York") != -1:
            #print(line,)
            items = line.strip().split('\t')
            ny_total += float(items[4])
            ny_con = ny_con + 1
            #print(items[4], " ", ny_con, " ", ny_total)
        elif line.find("San Francisco") != -1:
            #print(line,)
            items = line.strip().split('\t')
            sf_total += float(items[4])
            sf_con = sf_con + 1
#            print(items[4], " ", sf_con, " ", sf_total)

    ny_avg = ny_total/ny_con
    print('The average transaction amount based on %d transactions in New York is %.3f.' % (ny_con, ny_avg), file=open("output.txt", "a"))
    sf_avg = sf_total/sf_con
    print('The average transaction amount based on %d transactions in San Francisco is %.3f.' % (sf_con,sf_avg), file=open("output.txt", "a"))

    if (ny_total < sf_total):
        print('San Francisco has a higher average transaction amount than New York.', file=open("output.txt", "a"))
    else:
        print('New York has a higher average transaction amount than San Francisco.', file=open("output.txt", "a"))

parsefile('new_purchases.txt')
