# 🎭 Contributing to Apologize Machine

First of all, thank you for wanting to contribute! 
Whether it's adding more absurd reasons, fixing bugs, or adding new languages — every contribution is welcome.

## 🚀 Ways to Contribute

### 🐛 Bug Reports
- Found a reason that doesn't make sense? Open an issue!
- Program crashes? Open an issue!
- Generated an apology that's *too* reasonable? DEFINITELY open an issue!

### 💡 Feature Ideas
- New languages (we're thinking Klingon next)
- More dramatic consequences
- Integration with calendar apps (so it actually helps you remember)
- Web interface (because terminals aren't dramatic enough)

### 📝 Documentation
- Translation improvements
- Better examples
- Your success story (if any)

## 🛠️ Development Setup

```bash
# 1. Fork the repository
# 2. Clone your fork
git clone https://github.com/thinhjojo/apologize-machine.git
cd apologize-machine

# 3. Create a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 4. Run the program
python3 apologize_machine.py
```

## 📋 Coding Standards

We have exactly one coding standard:

**It should be funny.**

Beyond that:
- Use meaningful variable names (or hilariously misleading ones)
- Add comments when the joke is too complex
- Test your changes by running the program
- Make sure the UTF-8 encoding works (this is important for 4 languages)

## 🔄 Pull Request Process

1. Fork the repo
2. Create a branch: `git checkout -b feature/absurd-reason`
3. Add your absurd contribution
4. Test it works
5. Open a PR with a funny description
6. Wait for review (we're probably too busy forgetting things)

## 📜 Commit Message Guidelines

Your commit messages should be:
- Clear
- Descriptive
- Slightly dramatic

Examples:
```
feat: add more dog-related excuses
fix: cat no longer causes system crash
docs: clarify that capybaras are not included
refactor: make apologies even more apologetic
```

## 🗂️ Project Structure

```
apologize-machine/
├── apologize_machine.py  # Main program
├── README.md             # You're here
├── LICENSE               # Very important legal stuff
├── CONTRIBUTING.md       # This file
├── setup.py              # For pip installation
└── tests/
    └── test_apologize.py # Coming "soon" (TM)
```

## ❓ FAQ

**Q: Can I add my own reasons?**  
A: Yes! Just edit the `DATA` dictionary. More = merrier.

**Q: Why doesn't this actually help people remember things?**  
A: That's not a bug, it's a feature. The absurdity is the point.

**Q: Are capybaras actually available?**  
A: We wish.

**Q: Can I use this for my actual apologies?**  
A: Please don't. Just say "sorry" like a normal person.

## 📞 Contact

- Issue Tracker: GitHub Issues
- Email: thinhjojo@gmail.com
- Support: Just remember things, it's not that hard

---

*Remember: Every great contribution started with someone forgetting something important.*

*Together, we can help people forget... wait, no. Remember!*
