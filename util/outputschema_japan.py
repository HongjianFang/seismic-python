#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
# File Name : outputschema_japan.py
#
# Purpose :
#
# Creation Date : 14-09-2019
#
# Last Modified : Sat Sep 14 20:52:34 2019
#
# Created By : Hongjian Fang: hfang@mit.edu 
#
#_._._._._._._._._._._._._._._._._._._._._.*/

import pickle

schema = \
        {'Attributes':
                {
                    'evid':{'dtype':str,'format':'%16ld','null':'9999999999999999','width':16},
                    'Recordtype':{'dtype':str,'format':'%-1s','null':'-','width':1},
                    'year':{'dtype':int,'format':'%4ld','null':'9999','width':4},
                    'month': {'dtype': int, 'width': 2, 'null': 99},
                    'day': {'dtype': int, 'width': 2, 'null':99},
                    'hour': {'dtype': int, 'width': 2, 'null': 99},
                    'minute': {'dtype': int, 'width': 2, 'null': 99},
                    'second': {'dtype': int, 'width': 4, 'null': 9999},
                    'sec_std': {'dtype': int, 'width': 4, 'null': -999},
                    'lat_deg': {'dtype': int, 'width': 3, 'null': -99},
                    'lat_min': {'dtype': float, 'width': 4, 'null': -999},
                    'std_lat': {'dtype': float, 'width': 4, 'null': -999},
                    'lon_deg': {'dtype': int, 'width': 4, 'null': -999},
                    'lon_min': {'dtype': float, 'width': 4, 'null': -999},
                    'std_lon': {'dtype': float, 'width': 4, 'null': -999},
                    'depth': {'dtype': float, 'width': 5, 'null': -9999},
                    'std_dep': {'dtype': float, 'width': 3, 'null': -99},
#                    'amp_mag1': {'dtype': float, 'width': 2, 'null': -9},
                    'amp_mag1': {'dtype': str, 'width': 2, 'null': '-'},
                    'magtype1': {'dtype': str, 'width': 1, 'null': '-'},
                    #'amp_mag2': {'dtype': float, 'width': 2, 'null': -9},
                    'amp_mag2': {'dtype': str, 'width': 2, 'null': '-'},
                    'magtype2': {'dtype': str, 'width': 1, 'null': '-'},
                    'tttable': {'dtype': str, 'width': 1, 'null': '-'},
                    'hypoloc': {'dtype': str, 'width': 1, 'null': '-'},
                    'subsidinfo': {'dtype': str, 'width': 1, 'null': '-'},
                    'maxinten': {'dtype': str, 'width': 1, 'null': '-'},
                    'damgeclas': {'dtype': str, 'width': 1, 'null': '-'},
                    'tsunamiclas': {'dtype': str, 'width': 1, 'null': '9'},
                    'districtno': {'dtype': int, 'width': 1, 'null': '9'},
                    'regionno': {'dtype': int, 'width': 3, 'null': '-99'},
                    'regionname': {'dtype': str, 'width': 24, 'null': '-'},
                    'stano': {'dtype': int, 'width': 3, 'null': '-99'},
                    'hypoflag': {'dtype': str, 'width': 1, 'null': '-'},

                    'recordtype': {'dtype': str, 'width': 1, 'null': '-'},
                    'stacode': {'dtype': str, 'width': 6, 'null': '-'},
                    'stationno': {'dtype': int, 'width': 4, 'null': '-999'},
                    'blank': {'dtype': str, 'width': 1, 'null': '-'},
                    'seismotype': {'dtype': str, 'width': 1, 'null': '-'},
                    'date': {'dtype': int, 'width': 2, 'null': '-9'},
                    'phasename1': {'dtype': str, 'width': 4, 'null': '-'},
                    'arrhour1': {'dtype': int, 'width': 2, 'null': '-9'},
                    'arrmin1': {'dtype': int, 'width': 2, 'null': '-9'},
                    'arrsec1': {'dtype': float, 'width': 4, 'null': '-999'},
                    'phasename2': {'dtype': str, 'width': 4, 'null': '-'},
                    'arrmin2': {'dtype': int, 'width': 2, 'null': '-9'},
                    'arrsec2': {'dtype': float, 'width': 4, 'null': '-999'},
                    'maxamp1': {'dtype': int, 'width': 5, 'null': '-9999'},
                    'periodamp1': {'dtype': float, 'width': 3, 'null': '-99'},
                    'timeocc1': {'dtype': int, 'width': 3, 'null': '-99'},
                    'maxamp2': {'dtype': int, 'width': 5, 'null': '-9999'},
                    'periodamp2': {'dtype': float, 'width': 3, 'null': '-99'},
                    'timeocc2': {'dtype': int, 'width': 3, 'null': '-99'},
                    'maxamp3': {'dtype': int, 'width': 5, 'null': '-9999'},
                    'periodamp3': {'dtype': float, 'width': 3, 'null': '-99'},
                    'timeocc3': {'dtype': int, 'width': 3, 'null': '-99'},
                    'unitamp': {'dtype': str, 'width': 1, 'null': '-'},
                    'polarity1': {'dtype': str, 'width': 1, 'null': '-'},
                    'ampini1': {'dtype': int, 'width': 3, 'null': '-99'},
                    'polarity2': {'dtype': str, 'width': 1, 'null': '-'},
                    'ampini2': {'dtype': int, 'width': 3, 'null': '-99'},
                    'polarity3': {'dtype': str, 'width': 1, 'null': '-'},
                    'ampini3': {'dtype': int, 'width': 3, 'null': '-99'},
                    'unitinit': {'dtype': str, 'width': 1, 'null': '-'},
                    'duration': {'dtype': int, 'width': 3, 'null': '-99'},
                    'datayear': {'dtype': int, 'width': 2, 'null': '-9'},
                    'datamonth': {'dtype': int, 'width': 2, 'null': '-9'},
                    'dataflags1': {'dtype': str, 'width': 1, 'null': '-'},
                    'dataflags2': {'dtype': str, 'width': 1, 'null': '-'},
                    'dataflags3': {'dtype': str, 'width': 1, 'null': '-'},
                    'dataflags4': {'dtype': str, 'width': 1, 'null': '-'},
                    'dataweight': {'dtype': str, 'width': 1, 'null': '-'},
                    },
#        'Relations':{'origin':[]}
        'Relations':{'origin':['Recordtype', 'year', 'month', 'day', 'hour', 'minute', 'second', 'sec_std', 'lat_deg', 'lat_min', 'std_lat', 'lon_deg', 'lon_min', 'std_lon', 'depth', 'std_dep', 'amp_mag1', 'magtype1', 'amp_mag2', 'magtype2', 'tttable', 'hypoloc', 'subsidinfo', 'maxinten', 'damgeclas', 'tsunamiclas', 'districtno', 'regionno', 'regionname', 'stano', 'hypoflag'],
                    'arrival':['recordtype', 'stacode', 'stationno', 'blank', 'seismotype', 'date', 'phasename1', 'arrhour1', 'arrmin1', 'arrsec1', 'phasename2', 'arrmin2', 'arrsec2', 'maxamp1', 'periodamp1', 'timeocc1', 'maxamp2', 'periodamp2', 'timeocc2', 'maxamp3', 'periodamp3', 'timeocc3', 'unitamp', 'polarity1', 'ampini1', 'polarity2', 'ampini2', 'polarity3', 'ampini3', 'unitinit', 'duration', 'datayear', 'datamonth', 'dataflags1', 'dataflags2', 'dataflags3', 'dataflags4', 'dataweight'
                    ]}
}                    

with open("./japan_jma.pkl", "wb") as outf:
    pickle.dump(schema,outf)
                    



