# pskwebsite

The public website of MIT Phi Sigma Kappa. Redesigned Summer 2016. 

## Set-Up

Go to `/psk` directory. After you have `node.js` version 6.3.0 installed, you should be able to run the command `npm start` to run a local copy of the website. 

## Directory Structure

The HTML for the various sections are in `\views`. The style sheets are in `\css`. Often, either `event.css` or `\themes\psk.css` will be the files you are looking for. All of the code for each Angular components are in `\app` and the corresponding sub-folders. 

`index.html` puts all the JavaScript in one place and includes the Angular components.

## What is Angular?

Angular.js is a frontend development framework, which means that there are a lot of things that are easier about making websites if you put a little time into learning how to use them. In this website, we use Angular "components," which are chunks of HTML/JavaScript that behave on their own, and can be put into a bigger website whenever you want. The navigation bar is a component since it is a reusable, stand-alone part of the website. The pictures of brothers are components since each one has the same template. Being able to move these elements around in a flexible and intuitive way is pretty nice. 

## Adding / Updating Brothers' Info On Website

In the command line, run `edit_brothers.py`. This provides an interface for modifying the underlying JSON. It automatically determines "Senior" or "Freshman" for each brother when saved, unless the option `"year matches graduation"` is false, then the class year must be set on its own. This means, to move everyone from Freshmen to Sophomores or so on, just requires opening and saving around August. 
