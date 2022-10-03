engels_nederlands = { "last":"laatste", "week":"week", "the":"de",
"royal":"koninklijk", "festival":"feest", "hall":"hal",
"saw":"zaag", "first":"eerst", "performance":"optreden",
"of":"van", "a":"een", "new":"nieuw", "symphony":"symfonie",
"by":"bij", "one":"een", "world":"wereld", "leading":
"leidend", "modern":"modern", "composer":"componist",
"composers":"componisten", "two":"twee", "shed":"schuur",
"sheds":"schuren" }

nieuwe_zin = ""
zin = input("Geef een zin in het engels: ")
for woord in zin.split():
    nieuwe_zin += f"{engels_nederlands.get(woord, woord)} "
print(nieuwe_zin)