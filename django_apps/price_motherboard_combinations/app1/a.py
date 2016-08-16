def get_combinations(l):
    comb=[]
    le = len(l)
    i=0
    while i<le:
        j=i
        while j<le:
            comb.append((l[i],l[j]))
            j=j+1
        i=i+1
    return comb
def calc():
    cpus = [{"cpu":"i3","price":1000},{"cpu":"i5","price":2000},{"cpu":"i7","price":3000}]
    harddisks = [{"hdd":1,"price":1000},{"hdd":"2T","price":2000},{"hdd":"5T","price":3000},{"hdd":"7T","price":4000}]
    rams = [{"ram":1,"price":100},{"ram":2,"price":200},{"ram":4,"price":300},{"ram":8,"price":400}]
    ssds = [{"ssd":"200G","price":5000},{"ssd":"400G","price":6000},{"ssd":"800G","price":7000}]
    twoslots_harddisks=get_combinations(harddisks)
    twoslots_rams=get_combinations(rams)
    twoslots_ssds=get_combinations(ssds)

    result = []
    for cpu in cpus:
        for ram in rams:
            for harddisk in harddisks:
                for ssd in ssds:
                    total = cpu['price']+ram['price']+harddisk['price']+ssd['price']
                    result.append({
                        'cpu':cpu['cpu'],
                        'ram':ram['ram'],
                        'hd':harddisk['hdd'],
                        'ssd':ssd['ssd'],
                        'total':total
                        })
    for cpu in cpus:
        for twoslots_ram in twoslots_rams:
            for twoslots_harddisk in twoslots_harddisks:
                for twoslots_ssd in twoslots_ssds:
                    total = twoslots_ssd[0]['price']+twoslots_ssd[1]['price']\
                    +twoslots_harddisk[0]['price']+twoslots_harddisk[1]['price']\
                    +twoslots_ssd[0]['price']+twoslots_ssd[1]['price']
                    result.append({
                        'cpu':cpu['cpu'],
                        'ram':str(twoslots_ram[0]['ram'])+","+str(twoslots_ram[1]['ram']),
                        'hd':str(twoslots_harddisk[0]['hdd'])+","+str(twoslots_harddisk[1]['hdd']),
                        'ssd':str(twoslots_ssd[0]['ssd'])+","+str(twoslots_ssd[1]['ssd']),
                        'total':total
                        })
    return result
print calc()