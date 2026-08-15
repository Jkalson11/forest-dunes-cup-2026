#!/usr/bin/env python3
"""Transcribe the four Kohler cards into HTML, verifying every printed total.

Nothing is emitted unless each computed Out / In / Total matches the figure
printed on the physical card, the pars match, and the stroke indexes form a
clean 1-18 split. Source: photographs of the 2023 Golf Associates cards.
"""

TEES = ["Black", "Blue", "Green", "White", "Red"]

STRAITS = {
    "id": "straits",
    "name": "The Straits",
    "sub": "Whistling Straits &middot; Pete Dye, 1998",
    "when": "Saturday, 12:12",
    "names": ["Outward Bound", "Cross Country", "O&rsquo;Man", "Glory", "Snake",
              "Gremlin&rsquo;s Ear", "Shipwreck", "On the Rocks", "Down and Dirty",
              "Voyageur", "Sand Box", "Pop Up", "Cliff Hanger", "Widow&rsquo;s Watch",
              "Grand Strand", "Endless Bite", "Pinched Nerve", "Dyeabolical"],
    "par": [4,5,3,4,5,4,3,4,4,  4,5,3,4,4,4,5,3,4],
    "idx": [15,7,17,1,5,13,9,3,11,  12,6,18,14,16,4,10,8,2],
    "yds": {
        "Black": [493,597,188,494,603,409,221,506,442, 391,645,163,402,396,503,568,249,520],
        "Blue":  [405,533,180,451,563,378,205,470,412, 376,563,138,389,360,464,545,223,487],
        "Green": [370,521,166,414,543,360,185,429,384, 334,544,118,364,346,429,535,197,424],
        "White": [361,508,154,404,527,352,172,405,371, 320,519, 99,336,332,402,513,165,420],
        "Red":   [325,447,111,354,459,282,132,355,347, 304,479, 89,319,271,367,412,131,380],
    },
    "printed": {
        "Black": (3953,3837,7790), "Blue": (3597,3545,7142), "Green": (3372,3291,6663),
        "White": (3254,3106,6360), "Red": (2812,2752,5564),
    },
    "printed_par": (36, 36, 72),
    "ratings": [
        ("Black","77.2","152","0&ndash;2"), ("Blue","74.2","145","3&ndash;8"),
        ("Green","71.9","141","9&ndash;14"), ("White","70.4","137","15&ndash;20"),
        ("White/Red","68.6","134","21&ndash;25"), ("Red","66.4","129","26+"),
    ],
    "honours": "PGA Championship 2004 Singh, 2010 Kaymer, 2015 Day &middot; "
               "U.S. Senior Open 2007 Bryant &middot; Ryder Cup 2021, USA 19&ndash;Europe 9",
    "restrooms": "4, 9, 13",
}

IRISH = {
    "id": "irish",
    "name": "The Irish",
    "sub": "Whistling Straits &middot; Pete Dye, 2000",
    "when": "Friday, 8:31 and 3:24",
    "names": ["High Ground", "Giants Leap", "Sleeper", "Sandbanks", "Devil&rsquo;s Elbow",
              "Mulligan&rsquo;s Watch", "Troll", "Garden Creek", "Last Gaspe",
              "Shepherd&rsquo;s Post", "Lamb Chop", "Highland Trek", "Blind Man&rsquo;s Bluff",
              "Tullamore Dew", "Frog Water", "Deep Dye", "Irish Mist", "Black and Tan"],
    "par": [4,4,3,4,5,3,4,5,4,  4,3,4,3,5,4,4,4,5],
    "idx": [4,6,18,2,14,16,12,10,8,  5,15,13,17,11,1,3,7,9],
    "yds": {
        "Black": [400,372,147,489,570,160,372,555,484, 398,208,413,183,564,479,474,375,558],
        "Blue":  [387,360,138,443,517,149,363,542,409, 387,193,396,160,520,459,436,355,536],
        "Green": [369,347,128,432,501,135,344,501,322, 378,177,373,152,508,416,425,335,523],
        "White": [359,340,118,405,477,123,339,459,308, 361,169,349,145,469,370,383,325,493],
        "Red":   [301,309, 87,336,430, 97,320,392,263, 340,125,290,111,380,335,333,272,388],
    },
    "printed": {
        "Black": (3549,3652,7201), "Blue": (3308,3442,6750), "Green": (3079,3287,6366),
        "White": (2928,3064,5992), "Red": (2535,2574,5109),
    },
    "printed_par": (36, 36, 72),
    "ratings": [
        ("Black","75.6","146","0&ndash;2"), ("Blue","73.5","141","3&ndash;8"),
        ("Green","72.0","137","9&ndash;14"), ("White","70.3","133","15&ndash;20"),
        ("White/Red","67.9","127","21&ndash;25"), ("Red","65.6","122","26+"),
    ],
    "honours": "Palmer Cup 2005, USA 14&ndash;Europe 10",
    "restrooms": "5, 8, 13",
}

RIVER = {
    "id": "river",
    "name": "The River",
    "sub": "Blackwolf Run &middot; Pete Dye, 1988",
    "when": "Thursday, 1:43",
    "names": ["Snake", "Burial Mounds", "Gotcha", "Swan Lake", "Made in Heaven",
              "Jackknife", "Glencary", "Hell&rsquo;s Gate", "Cathedral Spires",
              "River and Marsh", "Rise and Fall", "Long Lagoon", "Tall Timber",
              "Blind Alley", "The Sand Pit", "Unter Der Linden", "Snapping Turtle",
              "Dyehard"],
    "par": [5,4,4,3,4,4,4,5,4,  3,5,4,3,4,4,5,3,4],
    "idx": [5,13,1,15,3,17,7,9,11,  14,6,2,10,16,18,8,12,4],
    "yds": {
        "Black": [610,377,468,219,427,388,426,532,361, 227,621,486,231,346,374,620,181,510],
        "Blue":  [564,370,410,195,400,361,401,524,337, 204,560,465,205,310,354,560,175,470],
        "Green": [526,355,395,185,388,333,374,492,316, 194,536,423,150,304,346,540,168,440],
        "White": [501,345,389,146,376,308,352,470,302, 175,522,372,135,294,329,511,153,415],
        "Red":   [411,310,295,117,275,265,298,401,238, 147,446,333,101,228,290,483,131,351],
    },
    "printed": {
        "Black": (3808,3596,7404), "Blue": (3562,3303,6865), "Green": (3364,3101,6465),
        "White": (3189,2906,6095), "Red": (2610,2510,5120),
    },
    "printed_par": (37, 35, 72),
    "ratings": [
        ("Black","76.2","151","0&ndash;2"), ("Blue","73.7","144","3&ndash;8"),
        ("Green","72.1","139","9&ndash;14"), ("White","70.3","132","15&ndash;20"),
        ("White/Red","68.0","127","21&ndash;25"), ("Red","65.7","123","26+"),
    ],
    "honours": "World Championships of Golf 1995 McCumber, 1996 Norman, 1997 Els &middot; "
               "U.S. Women&rsquo;s Open 1998 Pak, 2012 Choi",
    "restrooms": "3, 8, 12, 14",
}

MEADOW = {
    "id": "meadow",
    "name": "Meadow Valleys",
    "sub": "Blackwolf Run &middot; Pete Dye, 1988",
    "when": "Sunday, 9:49",
    "names": ["Fishing Hole", "Table Top", "Pine Valley", "Gamble", "Tree Stand",
              "Serpentine", "Goose Landing", "Wet and Wild", "Deer Hunt",
              "Quiver", "High Country", "Ledge Walk", "Chimney", "Nature&rsquo;s Course",
              "Mercy", "Rolling Thunder", "Maple Syrup", "Salmon Trap"],
    # Hole 7 read as the front's second par 5: the printed Out of 36 needs two,
    # Gamble is the other, and index 17 on a 520-yard hole is a reachable five.
    "par": [4,4,3,5,4,4,5,3,4,  4,5,4,4,4,3,5,3,4],
    "idx": [7,5,15,9,11,1,17,13,3,  10,14,2,8,6,16,12,18,4],
    "yds": {
        "Black": [392,446,182,565,403,475,520,240,485, 382,522,461,341,423,227,590,182,478],
        "Blue":  [368,402,176,539,380,470,494,187,462, 366,514,438,335,409,196,544,165,439],
        "Green": [349,385,158,516,362,444,488,176,432, 330,495,407,313,384,189,487,152,383],
        "White": [335,375,142,473,340,406,475,160,413, 320,487,395,304,376,150,478,138,373],
        "Red":   [281,278,110,428,314,341,426,112,307, 242,460,327,233,293,103,415, 92,303],
    },
    "printed": {
        "Black": (3708,3606,7314), "Blue": (3478,3406,6884), "Green": (3310,3140,6450),
        "White": (3119,3021,6140), "Red": (2597,2468,5065),
    },
    "printed_par": (36, 36, 72),
    "ratings": [
        ("Black","75.3","145","0&ndash;2"), ("Blue","73.3","139","3&ndash;8"),
        ("Green","71.5","136","9&ndash;14"), ("White","70.3","132","15&ndash;20"),
        ("White/Red","67.8","128","21&ndash;25"), ("Red","65.2","123","26+"),
    ],
    "honours": "U.S. Women&rsquo;s Open 1998 Pak, 2012 Choi",
    "restrooms": "3, 9, 11, 15",
}

COURSES = [RIVER, IRISH, STRAITS, MEADOW]   # trip order


def verify(c):
    bad = []
    for tee in TEES:
        y = c["yds"][tee]
        if len(y) != 18:
            bad.append(f'{c["name"]} {tee}: {len(y)} holes'); continue
        got = (sum(y[:9]), sum(y[9:]), sum(y))
        want = c["printed"][tee]
        if got != want:
            bad.append(f'{c["name"]} {tee}: computed {got} vs printed {want}')
    p = c["par"]
    got = (sum(p[:9]), sum(p[9:]), sum(p))
    if got != c["printed_par"]:
        bad.append(f'{c["name"]} par: computed {got} vs printed {c["printed_par"]}')
    if sorted(c["idx"]) != list(range(1, 19)):
        bad.append(f'{c["name"]} index not a permutation of 1-18')
    # Each nine takes one parity - which nine gets the odds varies by card.
    front, back = set(c["idx"][:9]), set(c["idx"][9:])
    odds, evens = set(range(1, 19, 2)), set(range(2, 19, 2))
    if {frozenset(front), frozenset(back)} != {frozenset(odds), frozenset(evens)}:
        bad.append(f'{c["name"]} nines do not split cleanly odd/even')
    if len(c["names"]) != 18:
        bad.append(f'{c["name"]} has {len(c["names"])} names')
    return bad


def nine(c, lo, hi, label):
    out = []
    for i in range(lo, hi):
        y = "".join(f'<td class="y">{c["yds"][t][i]:,}</td>' for t in TEES)
        out.append(f'<tr><td class="hole">{i+1}</td><td class="name">{c["names"][i]}</td>'
                   f'<td class="p">{c["par"][i]}</td><td class="x">{c["idx"][i]}</td>{y}</tr>')
    tot = "".join(f'<td class="y">{sum(c["yds"][t][lo:hi]):,}</td>' for t in TEES)
    out.append(f'<tr class="sum"><td></td><td>{label}</td><td class="p">{sum(c["par"][lo:hi])}</td>'
               f'<td class="x"></td>{tot}</tr>')
    return "\n".join("            " + r for r in out)


def block(c):
    head = "".join(f'<th class="y">{t}</th>' for t in TEES)
    grand = "".join(f'<td class="y">{sum(c["yds"][t]):,}</td>' for t in TEES)
    ratings = "\n".join(
        f'            <tr><td>{t}</td><td class="n">{r}</td><td class="n">{s}</td><td class="n">{h}</td></tr>'
        for t, r, s, h in c["ratings"])
    return f"""
    <div class="cardblock" id="card-{c["id"]}">
      <div class="card-title">
        <h3>{c["name"]}</h3>
        <span>{c["sub"]} &middot; Par {sum(c["par"])} &middot; {c["when"]}</span>
      </div>
      <div class="table-wrap">
        <table class="scorecard">
          <thead>
            <tr><th>No.</th><th>Hole</th><th class="p">Par</th><th class="x">Idx</th>{head}</tr>
          </thead>
          <tbody>
{nine(c, 0, 9, "Out")}
{nine(c, 9, 18, "In")}
            <tr class="grand"><td></td><td>Total</td><td class="p">{sum(c["par"])}</td><td class="x"></td>{grand}</tr>
          </tbody>
        </table>
      </div>
      <div class="card-foot">
        <div class="table-wrap ratings-wrap">
          <table class="ratings">
            <thead>
              <tr><th>Tee</th><th class="n">Rating</th><th class="n">Slope</th><th class="n">For index</th></tr>
            </thead>
            <tbody>
{ratings}
            </tbody>
          </table>
        </div>
        <div class="card-notes">
          <p><b>Honours.</b> {c["honours"]}</p>
          <p><b>Restrooms</b> following holes {c["restrooms"]}.</p>
        </div>
      </div>
    </div>
"""


if __name__ == "__main__":
    problems = []
    for c in COURSES:
        bad = verify(c)
        problems += bad
        tees = len(TEES)
        print(f'{c["name"]:<16} {"OK" if not bad else "MISMATCH"}  '
              f'({tees} tee sets, par {sum(c["par"])}, black {sum(c["yds"]["Black"]):,})')
        for b in bad:
            print("    ", b)
    if problems:
        raise SystemExit("refusing to emit HTML with unverified numbers")
    print(f'\nAll {len(COURSES) * len(TEES)} tee sets match their printed totals.')
    open("cards_block.html", "w").write("".join(block(c) for c in COURSES))
    print("wrote cards_block.html")
