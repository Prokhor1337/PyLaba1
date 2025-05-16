def search_and_sort(phones, keyword="", sort_by="price"):
    keyword = keyword.lower()
    filtered = [p for p in phones if keyword in p["title"].lower() or keyword in p["description"].lower()]
    return sorted(filtered, key=lambda x: x[sort_by])
