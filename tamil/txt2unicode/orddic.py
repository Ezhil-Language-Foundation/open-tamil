try:
    # python 2.7 defaults comes with collections module
    from collections import OrderedDict
except Exception as e:
    try:
        # In python 2.2 to 2.6, user need to install ordereddict via pip
        from ordereddict import OrderedDict
    except Exception as e:
        print(e, "No module found to import OrderedDict. So using normal dict itself")
        OrderedDict = dict 
    # end of try:
# end of try:
