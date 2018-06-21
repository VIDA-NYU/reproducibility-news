# Contributing

We would absolutely love any pull requests to contribute materials to our RSS feed of curated materials about reproducibility. If you add resources to our feed, the contributions will be tweeted out via the [@ReproFeed](https://twitter.com/ReproFeed) twitter bot, and added to the directory on [reproduciblescience.org](https://reproduciblescience.org/directory).

## Best Practices for Contributing
* Make sure that the resource you are suggesting isn't already in the feed. 
* Make sure the resource you are suggesting is open access. This means that anyone should be able to access, read, and/or download it without having to pay money or login.
* Be sure to add at least one tag to the resource. You can find a list of tags in the README file in this repository.

## Workflow
If you'd like to contribute the RSS feed, then you need to edit the [`news.yaml`](https://github.com/ViDA-NYU/reproducibility-news/blob/master/news.yaml) file in this repository. When you navigate to the file, there's a pencil icon on the top right hand corner. If you click that, GitHub will ask you to fork the repository like so:

![](https://user-images.githubusercontent.com/426784/41747015-7d7aa0e2-757a-11e8-96ed-c096d3fd0148.png)

Do click the button that lets you fork the repository. Afterwards, you'll find a copy of the repository in your account. Edit the `news.yaml` file in *your* fork of this repository. At the top of the file, add the follow template:
     
     ---
     title: |
       Some meaningful title here (will be tweeted out). Add two spaces before title
     link: link to the original article or publication
     date: 2018-01-21 00:00:00
     tags: [reproducibility talk, reproducible paper]
     description: |
       Multi-line description here. Will show up in RSS readers.
       Like the title field, be careful not to forget the indentation (2 spaces).
              
You should at least change the title, date (when the resource was created), tags (you must have one, but can have many separated by a comma in the square brackets), and brief description. The description can be multi-line or one line. 

Please make sure you use a tag from the approved list in the README file from the original repository, and that you have two lines between the description of the current entry and the title of the next entry. After you are finished, at the bottom of the web page you should see a space to add a descriptive message about your changes, and a button that says 'Commit'. After you write your concise, descriptive message about your changes, click that button!

You should now be able to see the changes in your `news.ymal` file. To contribute your changes back to our original repository, you need to click the 'New pull request' button in the overview page of your repository, and go through the steps with GitHub. Make sure you are comparing the `master` branch of `Vida-NYU/reproducibility-news` to the `my-item-for-feed` branch of `yourname/reproducibility-news`.
  
You can also edit the file using standard GitHub workflow: 

1. Fork the project (the second button to the left under the title of the repo)
2. Clone your fork to your computer.

    * From the command line: `git clone https://github.com/<USERNAME>/reproducibility-news.git`

3. Change into your new project folder.

    * From the command line: `cd reproducibility-news`
4. [optional]  Add the upstream repository to your list of remotes.
    * From the command line: `git remote add upstream https://@gitlab.com:vida-nyu/reproducibility-news.git`

5. Create a branch for your new contribution.

    * From the command line: `git checkout -b my-item-for-feed`

6. Make changes to the `news.yaml`:
    * At the top of the file, add the follow template:
     
                ---
                title: |
                  Some meaningful title here (will be tweeted out). Add two spaces before title
                link: link to the original article or publication
                date: 2018-01-21 00:00:00
                tags: [reproducibility talk, reproducible paper]
                description: |
                  Multi-line description here. Will show up in RSS readers.
                  Like the title field, be careful not to forget the indentation (2 spaces).
              
    * Change the title, date (when the resource was created), tags (you must have one, but can have many separated by a comma in the square brackets), and a brief description. The description can be multi-line or one line.
    * Make sure you use a tag from the approved list in the README file of this repository.
    * Make sure you have two lines between the description of the current entry and the title of the next entry. 
    
7. Commit your changes. From the command line:

    * `git add <FILE-NAMES>`
    * `git commit -m "A descriptive commit message"`
    
8. While you were working some other changes might have gone in and break your stuff or vice versa. This can be a *merge conflict* but also conflicting behavior or code. Before you test, merge with master.

    * `git fetch upstream`
    * `git merge upstream/master`
    
9. Push the branch, uploading it to GitHub.

     * `git push origin my-item-for-feed`
     
10. Make a "Pull Request" from your branch here on GitHub, using the button in the repository homepage. Make sure you are comparing the `master` branch of `Vida-NYU/reproducibility-news` to the `my-item-for-feed` branch of `yourname/reproducibility-news`.

The following was adapted from [ProjectPorcupine's](https://github.com/TeamPorcupine/ProjectPorcupine)'s [CONTRIBUTING.md](https://github.com/TeamPorcupine/ProjectPorcupine/blob/master/CONTRIBUTING.md). 

## That's it!

Thanks for your contribution!

