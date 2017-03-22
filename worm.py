# -*- coding: utf-8 -*-
import requests
from pyquery import PyQuery as pq
import codecs
import json


def list_to_str(lists):
    res = "["
    for xx in lists:
        res += xx + ", "
    res = res[0:-2] + "]"
    return res


def get_detail_basic(detail_url):

    try:
        res = requests.get(detail_url)
    except:
        return "error"

    info = pq(res.text).find("div.titleinfo")
    table_basic = info("table.section.basic")
    basic = pq(table_basic.find("table.data"))
    basic = pq(basic.html())

    staff_data = {}
    for xx in basic("div").find("tr"):
        xx = pq(xx)
        key = xx.find("th").html()
        value = xx.find("a").html()
        if value is None:
            value = xx.find("td").html()
        staff_data[key] = value
    return json.dumps(staff_data, encoding="UTF-8", ensure_ascii=False)


def get_detail_staff(detail_url):
    try:
        res = requests.get(detail_url)
    except:
        return "error"

    info = pq(res.text).find("div.titleinfo")
    table_staff = info("table.section.staff")
    staff = pq(table_staff.find("table.data"))
    staff = pq(staff.html())

    staff_data = {}
    for xx in staff("tr"):
        xx = pq(xx)
        key = xx.find("th").html()
        value = xx.find("a").html()
        staff_data[key] = value
    return json.dumps(staff_data, encoding="UTF-8", ensure_ascii=False)


def get_detail_cast(detail_url):
    try:
        res = requests.get(detail_url)
    except:
        return "error"

    info = pq(res.text).find("div.titleinfo")
    table_cast = info("table.section.cast")
    cast = pq(table_cast.find("table.data"))
    cast = pq(cast.html())

    cast_data = {}
    for xx in cast("tr"):
        xx = pq(xx)
        key = xx.find("th").html()
        value = xx.find("a").html()
        cast_data[key] = value
    return json.dumps(cast_data, encoding="UTF-8", ensure_ascii=False)


def get_today():
    response = requests.get("http://cal.syoboi.jp/")
    d = pq(response.text)
    table = d("table").find(".v3boxContainer")
    three_day = pq(table.html())
    out = codecs.open("today.txt", "w+", "utf-8")

    lists = []

    today = three_day('tr').find('td').eq(1).html()
    today = pq(today)
    today = pq(today.html())
    today = today('div').html()
    today = pq(today)
    for xx in today("div").find(".pid-item"):
        inner = pq(pq(xx).html())
        inner_part1 = inner("a.v3title")
        inner_part2 = inner("a.v3ch")

        time = pq(xx).attr("title")
        detail_site = "http://cal.syoboi.jp" + inner_part1.attr("href")
        name = inner_part1.html()
        tv_company = inner_part2.html()
        count = inner.find("span.count").html()
        subtitle = inner.find("span.subtitle").html()

        item_dict = {"time": time, "detail": detail_site, "name": name, "company": tv_company,
                     "count": count, "subtitle": subtitle}
        data = json.dumps(item_dict, encoding="UTF-8", ensure_ascii=False)
        lists.append(data)
    result = list_to_str(lists)
    out.write(result)
    out.write("\n")
    out.close()
    return result


def get_before():
    response = requests.get("http://cal.syoboi.jp/")
    d = pq(response.text)
    table = d("table").find(".v3boxContainer")
    three_day = pq(table.html())
    out = codecs.open("before.txt", "w+", "utf-8")

    lists = []

    before = three_day('tr').find('td').eq(0).html()
    before = pq(before)
    before = pq(before.html())
    before = before('div').html()
    before = pq(before)
    for xx in before("div").find(".pid-item"):
        inner = pq(pq(xx).html())
        inner_part1 = inner("a.v3title")
        inner_part2 = inner("a.v3ch")

        time = pq(xx).attr("title")
        detail_site = "http://cal.syoboi.jp" + inner_part1.attr("href")
        name = inner_part1.html()
        tv_company = inner_part2.html()
        count = inner.find("span.count").html()
        subtitle = inner.find("span.subtitle").html()

        item_dict = {"time": time, "detail": detail_site, "name": name, "company": tv_company,
                     "count": count, "subtitle": subtitle}
        data = json.dumps(item_dict, encoding="UTF-8", ensure_ascii=False)
        lists.append(data)
    result = list_to_str(lists)
    out.write(result)
    out.write("\n")
    out.close()
    return result


def get_tomorrow():
    response = requests.get("http://cal.syoboi.jp/")
    d = pq(response.text)
    table = d("table").find(".v3boxContainer")
    three_day = pq(table.html())
    out = codecs.open("tomorrow.txt", "w+", "utf-8")

    lists = []

    tomorrow = three_day('tr').find('td').eq(2).html()
    tomorrow = pq(tomorrow)
    tomorrow = pq(tomorrow.html())
    tomorrow = tomorrow('div').html()
    tomorrow = pq(tomorrow)
    for xx in tomorrow("div").find(".pid-item"):
        inner = pq(pq(xx).html())
        inner_part1 = inner("a.v3title")
        inner_part2 = inner("a.v3ch")

        time = pq(xx).attr("title")
        detail_site = "http://cal.syoboi.jp" + inner_part1.attr("href")
        name = inner_part1.html()
        tv_company = inner_part2.html()
        count = inner.find("span.count").html()
        subtitle = inner.find("span.subtitle").html()

        item_dict = {"time": time, "detail": detail_site, "name": name, "company": tv_company,
                     "count": count, "subtitle": subtitle}
        data = json.dumps(item_dict, encoding="UTF-8", ensure_ascii=False)
        lists.append(data)
    result = list_to_str(lists)
    out.write(result)
    out.write("\n")
    out.close()
    return result


#print get_before()
#print get_today()
#print get_tomorrow()
#print get_detail_basic("1")
#get_detail_basic("http://cal.syoboi.jp/tid/4426#399644")
#get_detail_staff("http://cal.syoboi.jp/tid/4426#399644")
#get_detail_cast("http://cal.syoboi.jp/tid/4426#399644")


