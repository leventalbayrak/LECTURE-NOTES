
---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*

---

# Source Control and Git

## Table of Contents
- [Introduction: Why Version Control?](#introduction-why-version-control)
- [Limitations of Cloud Sync Services](#limitations-of-cloud-sync-services)
- [Version Control Concepts](#version-control-concepts)
- [Git Core Concepts](#git-core-concepts)
- [Git vs GitHub](#git-vs-github)
- [Basic Git Workflow](#basic-git-workflow)
- [Branching and Merging](#branching-and-merging)
- [GitHub Classroom Workflow](#github-classroom-workflow)
- [Assignment Submission and Grading](#assignment-submission-and-grading)

---

## Introduction: Why Version Control?

Before diving into Git, let's understand why we need version control systems in the first place.

### Cloud Storage: Google Drive and Dropbox

You're probably familiar with cloud storage services like Google Drive and Dropbox. These services:
- Watch a folder on your computer continuously
- Compare local files with cloud copies
- Automatically synchronize any changes
- Keep all copies (laptop, phone, cloud) in the same state
- Use timestamps to resolve conflicts between devices

**How it works:**
1. Install Google Drive/Dropbox on your computer
2. Point it to a folder to watch
3. A background program constantly monitors for changes
4. When it detects a difference, it updates the cloud
5. The cloud then syncs to all your other devices

This is excellent for photos and personal files, but has serious limitations for software projects.

---

## Limitations of Cloud Sync Services

### Problem 1: Limited Rollback Capability

While Google Drive does have basic version history (30 days / 100 revisions), it has significant limitations compared to what we need for software projects:

- **Limited retention period** - Only 30 days or 100 revisions
- **No branching or merging capabilities** - Can't work on parallel features
- **Can't handle conflicts intelligently** - No smart merging of changes
- **No meaningful commit messages** - Just timestamps, no descriptions of why changes were made
- **Not designed for code/text collaboration** - Made for documents, not software
- **No rollback of entire project states** - Can't restore multiple related files to a specific point in time together

For a Word document with undo, this might be enough. For software projects with multiple files and team members, it falls short.

### Problem 2: Vulnerable to Destructive Changes

**Scenario:** You're working on a group project with shared Google Drive access.

- You work all week on the project
- One group member never logs in or communicates
- Saturday 1 AM, they log in and make random changes
- Sunday morning, you discover everything is destroyed

**Result:** Your work is gone. There's nothing you can do about it.

### Problem 3: Real Cost for Companies

For students, losing a project means:
- Lost points on homework
- Frustration and sadness

For companies, the same issue means:
- Lost engineering hours
- Real money wasted
- Potential business impact
- The clock is always ticking, resources are being charged

**Companies cannot afford these risks.**

---

## Version Control Concepts

To solve these problems, we need a system with specific features:

### Key Requirements

To be clear: **automatic synchronization isn't inherently bad**. It's excellent for personal files and photos. The problem arises with collaborative software projects where you need:

1. **Track who's making changes** - Know who to hold accountable
2. **Deliberate checkpoints (commits)** - Changes should be intentional, not automatic
3. **Local changes first** - Work on changes locally without affecting the server
4. **Descriptive snapshots** - Write a description of what changed and why
5. **Ability to review before sharing** - Check your work before it goes live
6. **Coordination between team members** - Control when and how changes are integrated
7. **Manual push to server** - Only upload when you're ready
8. **Comprehensive rollback capabilities** - Restore entire project states across multiple files

### The Solution: Commits

A **commit** is a snapshot of your project at a specific point in time.

- **Commit = Snapshot** = Save (Ctrl+S) locally on your computer
- **Push = Upload** = Send your commits to the server
- **Repository = Folder** with version history

Instead of just having "the current version," you have:
- Version 1 (2 months ago)
- Version 2 (1 week ago)
- Version 3 (current)

Each version is linked in a chain, and you can:
- Rollback to any previous version
- See exactly what changed between versions
- Know who made each change and when

---

## Git Core Concepts

### What is Git?

**Git is software** - not a company, not a service - that handles version control.

Git's job:
- Take snapshots (commits) of your project
- Remember which snapshots were taken by which person
- Keep track of the entire history
- Correctly merge changes from different developers
- Handle Internet communications to sync with servers

### Repository Structure

A **repository** contains:
- Your project files
- A complete history of all versions
- Metadata about who made changes and when

Think of it like a timeline:
```
Version 1 → Version 2 → Version 3 → Version 4 (latest)
```

Each version is a commit with:
- A snapshot of all tracked files
- A description (commit message)
- Author information
- Timestamp

### Example: Website Development

**Scenario:** You want to change the title of a website from "cat website" to "CAT WEBSITE"

**Without version control:**
- Make changes directly to the live server
- Dangerous! What if you make a mistake while editing?
- Changes go live immediately
- No way to test first

**With Git:**
1. Download the full repository history to your computer
2. Make your changes locally (not affecting the live site)
3. Test and verify the changes work
4. Show it to friends, check spelling
5. Once you're happy, commit (snapshot) the changes
6. Push the commit to the server
7. The server now has your new version
8. If you realize later you made a mistake, rollback to the previous version

### Version Chains and Rollback

Because you keep the chain of versions:
```
V1 → V2 → V3 → V4 (oops, has a bug!)
```

You can rollback:
```
V1 → V2 → V3 (serve this version again)
```

This is **very powerful** for:
- Collaboration
- Complicated projects
- When you need to make changes without breaking things

---

## Branching and Merging

### Branching

You can **branch off** from the main timeline to work on parallel features:

```
Main:    V1 → V2 → V3 → V4 → V5
                    ↓
Branch:            V3a → V3b → V3c
```

- Main development continues on the main branch
- You work on your feature on a separate branch
- When done, merge your branch back into main
- Git is smart enough to combine changes from multiple people

### Merging

Git can merge changes from different developers working on different parts of the code.

**It works like Google Docs:**
- Multiple people can edit different parts simultaneously
- As long as you're not overlapping, it works perfectly
- But Git adds accountability and snapshots you can revert

### Conflict Detection

When two people change the same thing:
- One person changes "cat" to "bat"
- Another person changes "cat" to "rat"

Git will:
- Detect the conflict
- Show you both versions
- Let you decide which one to keep

Example diff display:
```
- cat website        (removed, shown in red)
+ CAT WEBSITE        (added, shown in green)
```

---

## Git vs GitHub

### Git (The Software)

- Git is **local software** installed on your computer
- Like Microsoft Office (Word, Excel, PowerPoint)
- A tool you use as part of your development workflow
- Open-source and free
- Works offline

### GitHub (The Service)

- GitHub is a **company** (owned by Microsoft)
- Provides **cloud storage** for Git repositories
- When Git needs to push, you tell it "push to GitHub"
- GitHub is just data storage that works really well with Git

**Analogy:** Git is like Word, GitHub is like OneDrive

### Other Services

GitHub isn't the only option:
- **GitLab** - Similar service, different company
- **Bitbucket** - Another alternative
- **Self-hosted Git servers** - Many companies run their own

### Why Companies Run Their Own Servers

**Security and control:**
- GitHub is run by Microsoft
- If Microsoft bans you (for any reason), you lose access
- This has happened to people working on projects for 10+ years
- Private companies can refuse service
- Companies want control over their code
- Running your own Git server eliminates this dependency

---

## Basic Git Workflow

### The Three Steps: Add, Commit, Push

#### 1. `git add` - Stage Files

```bash
git add filename.txt
```

- Adds files to a **staging area**
- Not all files need to be tracked
- You can choose which files to include in the commit
- Temporary files or personal notes don't need to be shared

**Why stage?**
You might have many files in your folder:
- Source code (track this)
- Temporary test files (don't track)
- Personal scratch notes (don't track)

Staging lets you select exactly what to snapshot.

#### 2. `git commit -m "message"` - Create Snapshot

```bash
git commit -m "Changed website title to capital letters"
```

- Creates a snapshot of staged files
- **Must include a message** describing what changed
- Message should be meaningful, not random letters
- The commit is saved **locally** (not on the server yet)

**Important:** Once you commit, you've created a new version in your local repository.

#### 3. `git push` - Upload to Server

```bash
git push
```

- Sends your commits to the remote server (like GitHub)
- Can push multiple commits at once
- No limit on how many times you can push

### Tracking Changes: Diffs

Git intelligently stores your file history. While it appears to track line-by-line changes when you view diffs, Git actually stores snapshots efficiently using compression and delta encoding behind the scenes. This means you get the benefits of both full snapshots (can restore any version completely) and space-efficient storage (doesn't waste space on duplicate data).

When you have a file with 2000 lines and change one line:
- Git can efficiently store just the changes
- But maintains complete version history
- You can restore any previous version in full

This makes Git very efficient while keeping all your history accessible.

**Viewing changes:**
- Green text with `+` prefix: Added lines
- Red text with `-` prefix: Removed lines

### Accountability

Diffs provide accountability:
- "I worked 15 hours on this!"
- Open the commit → see exactly what changed line by line
- If you only changed one line, we know you didn't work 15 hours

---

## Branching and Merging

### Creating Branches

```bash
git branch feature-name
git checkout feature-name
```

Branches let you:
- Work on experimental features
- Keep the main branch stable
- Test changes before merging

### Merging Branches

```bash
git checkout main
git merge feature-name
```

Git automatically merges:
- Changes that don't conflict
- Multiple developers' work

When conflicts occur:
- Git shows you both versions
- You manually resolve the conflict
- Commit the resolved version

---

## GitHub Classroom Workflow

### Step 1: Accept the Assignment

1. Instructor provides a GitHub Classroom link
2. Click the link (while logged into GitHub)
3. GitHub Classroom automatically creates a personal repository for you based on the assignment template
4. Repository name: `assignment-1-yourname`
5. This repository is **in the cloud**, not on your computer yet

**Note:** GitHub Classroom creates your own personal repository based on the assignment template. While this is similar to "forking," your repository is independent - you won't be submitting pull requests back to the original. Think of it as getting your own private copy of the assignment that only you and the instructor can access.

### Step 2: Clone the Repository

```bash
git clone https://github.com/classroom/assignment-1-yourname.git
```

**Clone** means:
- Make a copy of the remote repository on your local computer
- Link the local copy to the remote
- Now `git push` knows where to send your changes

### Step 3: Work on the Assignment

1. Open the cloned folder in VS Code or your terminal
2. Make changes to the code
3. Test your work

### Step 4: Commit Your Changes

```bash
git add .
git commit -m "Implemented feature X"
```

You can commit as many times as you want:
- Work during lunch → commit
- Come back → work more → commit again
- Multiple commits are fine

### Step 5: Push to GitHub

```bash
git push
```

- Push before the deadline
- You can push as many times as you want
- Only the commits pushed before the deadline count

---

## Assignment Submission and Grading

### Critical Rule: Push Before the Deadline

**Only commits pushed to GitHub before the deadline count.**

Even if you:
- Worked all week on the assignment
- Committed locally many times
- But pushed after the deadline

**Result: Assignment not accepted.**

Why? From the instructor's perspective:
- You kept a "secret diary" of your work
- Never showed it during the required timeframe
- Like a client who paid $50,000 for a website
- They don't care if it worked 5 minutes ago
- They care if it works **right now**

### Automated Grading Process

1. **During the assignment period (Week 1):**
   - You commit and push multiple times
   - Instructor doesn't touch your repository yet

2. **Starting around end of Week 1:**
   - Instructor's automated server picks up your latest commit
   - Creates a **feedback branch** from that commit
   - Runs tests and provides feedback
   - You see results in a README file on the feedback branch

3. **Continue working (Week 2):**
   - Read the feedback
   - Make more commits
   - Push again
   - Instructor creates another feedback branch from new commit
   - This repeats until the deadline

4. **After the deadline:**
   - One final feedback run
   - This determines your actual grade

### Understanding Feedback Branches

```
Your commits:     V1 → V2 → V3 → V4 → V5 → V6
                       ↓       ↓            ↓
Feedback branches:  FB1     FB2          FB3 (final grade)
```

- Each feedback branch is tied to a specific commit
- If FB1 says you failed, but you fixed it in V3, ignore FB1
- Wait for FB2 to see if V3 passes
- Don't panic and make unnecessary changes

**Common mistake:**
- Student gets FB1: "Failed"
- Reads FB1, assumes current work also fails
- Makes changes in panic
- But their V3 actually passed - they didn't wait for FB2
- New changes (V4) introduce bugs and fail
- Deadline hits on V4 = assignment fails

**Lesson:** Be patient. Each feedback is for a specific commit. Keep working methodically.

### Test Cases and Expected Outputs

- Assignments will provide test cases
- You'll see expected outputs
- Automated grading system runs your code against these tests
- Sometimes there are bugs in the grading system
- Instructor will communicate if there are mistakes

### Getting Help

- Tutors are available
- Use the class email/Teams
- Don't wait until the last minute
- Git setup can cause authorization issues, conflicts, etc.
- Start early to resolve problems

---

## Important Reminders

### Installation Required

Make sure you have installed:
- Git (the software)
- VS Code or your preferred editor
- Created a GitHub account (student benefits recommended)

### GitHub Student Benefits

If you're denied GitHub student benefits:
- Be persistent with support
- Explain you need it for class
- Don't let them push you around
- Your experience affects their brand reputation
- Companies care about word-of-mouth from students who become IT professionals

### Commit Message Best Practices

Good commit messages:
```
"Added user authentication feature"
"Fixed bug in shopping cart calculation"
"Updated homepage title styling"
```

Bad commit messages:
```
"ABCDFG"
"stuff"
"changes"
```

### Key Commands Summary

```bash
# Clone a repository
git clone <url>

# Check status
git status

# Stage files
git add <filename>
git add .              # Add all files

# Commit changes
git commit -m "Your message here"

# Push to remote
git push

# View differences
git diff
```

### Essential Git Commands for This Class

**Start with these core commands:**
- `git add` - Stage your changes
- `git commit` - Save a snapshot
- `git push` - Upload to server

**Additional useful commands:**

Once you're comfortable with the basics, these commands will be helpful:

```bash
git status          # See what's changed (use this often!)
git pull            # Get updates from remote (important for feedback!)
git log             # View commit history
git diff            # See what changed before committing
```

**Important note about `git pull`:**
If you work on two different computers (e.g., a lab computer and a personal laptop), you **must** run `git pull` before you start working to get the latest changes from the remote repository. If you forget to pull first and make changes on both computers, you'll create merge conflicts that can be difficult to resolve. Always pull first, then work, then commit and push.

**Example workflow:**
```bash
git status                          # Check what's changed
git add filename.py                 # Stage specific file
git commit -m "Completed task 1"    # Create snapshot with message
git push                            # Upload to GitHub
```

Branching and merging are advanced topics. Don't worry about mastering them immediately - focus on the core workflow first.

---

## Conclusion

Version control with Git is:
- An industry-standard skill
- Essential for software development
- More powerful than cloud sync for code projects
- Provides accountability, history, and safety

Think of Git like Microsoft Office:
- It's a tool you use as part of your workflow
- You've been using Office since you were a student
- Git is the same for developers

You don't have to love it, but **you have to learn it**.

---
*© 2026 Levent Albayrak. Distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).*
