def greg2jul(year, month, day, hour, minute, second):

    aData = (14 - month) // 12
    yData = year + 4800 - aData
    mData = month + 12 * aData - 3
    julian_day = day + (153 * mData + 2) // 5 + 365 * yData + yData // 4 - yData // 100 + yData // 400 - 32045
    julian_day += hour / 24 + minute / 1440 + second / 86400
    return julian_day
  
