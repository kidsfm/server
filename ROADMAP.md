# Roadmap for vaangroup.com

This Doc lists issues/ideas and next steps for the next releases of this project






## Next minor release

The tech debt list for version 0.1.x



### Update app.production.coffee

* ✔ remove wordpress related imports/configs
* ✔ setup image_pipeline



### Update JS and CSS pipelines

* this will output relative paths making it easier to reference main files in sub directories
* update `!= css()` to `!= css(/)`
* update `!= js()` to `!= js(/)`



### Add excludes to image_pipeline

* favicon.ico doesn't need compression






## Next major release

The tech debt list for version 1.x.x


### Update Roots build recipe

* build a `.json` file that models the site-map (pages and copy)
* setup unit or end-to-end tests to verify that there are html files for each page sepcified in the '.json' specs
* create `.jade` templates and configure them to fetch copy for each page from site-map model
* add plugin to CMS to enable product owners to reset the site to the latest stable build.
* Note: this will essentially be a factory reset type thing


