from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    # return 'Hello World!'
    return render_template('index.html')

@app.route('/blog/')
def blog():
    posts = [
        {'title': "Summer Horror Flicks",
        'author': "Tim Johnson",
        'date': "May 5th, 2022",
        'body': "\tZombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro. De carne lumbering animata corpora quaeritis. Summus brains sit​​, morbo vel maleficia? De apocalypsi gorger omero undead survivor dictum mauris. Hi mindless mortuis soulless creaturas, imo evil stalking monstra adventus resi dentevil vultus comedat cerebella viventium. Qui animated corpse, cricket bat max brucks terribilem incessu zomby. The voodoo sacerdos flesh eater, suscitat mortuos comedere carnem virus. Zonbi tattered for solum oculi eorum defunctis go lum cerebro. Nescio brains an Undead zombies. Sicut malus putrid voodoo horror. Nigh tofth eliv ingdead."
        },
        {'title': "Bootcamp, Here We Go!",
        'author': "Timothy Tyson Alan Johnson",
        'date': "April 24th, 2022",
        'body': "\tThere are two ways to write error-free programs; only the third one works. (Alan J. Perlis) You can either have software quality or you can have pointer arithmetic, but you cannot have both at the same time. (Bertrand Meyer) Computers are useless. They can only give you answers. (Pablo Picasso) Good programmers use their brains, but good guidelines save us having to think out every case. (Francis Glassborow) The Web is like a dominatrix. Everywhere I turn, I see little buttons ordering me to Submit. (Nytwind)"
        },
        {'title': "The Time Machine Works...Kind Of",
        'author': "Timediah Johnsmith",
        'date': "February 12th, 1745",
        'body': "\tDeadlights jack lad schooner scallywag dance the hempen jig carouser broadside cable strike colors. Bring a spring upon her cable holystone blow the man down spanker Shiver me timbers to go on account lookout wherry doubloon chase. Belay yo-ho-ho keelhaul squiffy black spot yardarm spyglass sheet transom heave to."
        },
        {'title': "Fall is the Best Season, Fight Me",
        'author': "Jim Thompson",
        'date': "October 3rd, 2019",
        'body': "\tLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        }
        ]
    return render_template('blog.html', posts=posts)
        

app.run(debug=True)