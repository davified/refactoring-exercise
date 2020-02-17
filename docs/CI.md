# Continuous Integration (CI)

When we have tests, we can take it to the next level and implement another agile practice: continuous integration (CI).

## What is continuous integration

Continuous integration (of code) is a development practice that requires developers to integrate code into a shared repository several times a day. Each check-in is then verified by an automated build, allowing teams to detect problems early. By integrating regularly, you can detect errors quickly, and locate them more easily.

## How do we do it

There are several CI tools that you can use (e.g. [CircleCI](https://circleci.com/), [GoCD](https://www.gocd.org/), [TravisCI](https://travis-ci.org/), etc). For this workshop, we will use CircleCI.

## Steps for setting up your CI pipeline

- Create CircleCI account: https://circleci.com/ (free)
- Create circleci project. Visit https://circleci.com/dashboard, login and click on 'Add Projects' on the left panel. Click on 'Set up project' for the git repo of your choice
- Add [.circleci/config.yml](../.circleci/config-reference.yml) to your repo. Commit and push your code to GitHub
- Go to the page of the CircleCI project that you just created, a sit back and watch circleci run your tests!
