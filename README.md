# IDA Color Schemer

The main idea is to create a tool to easily design IDA color schemes outside IDA.

This will hopefully allow simplifying & automating the generation of color schemes and help create colorblind-friendly settings.


## How this works

IDA has HTML export support. So we already have a display-engine that we can use to emulate IDA.
What is left is to map the settings to the HTML.

1. Export color scheme from IDA to generate base template
2. Replace all colors in the scheme to ensure uniqueness
3. Load new scheme into IDA
4. Bleed from eyes
5. Export HTML from IDA
6. Replace `style="color:#123456"` with `class="cls_123456"` in the HTML file
7. Add a stylesheet with the relevant classes

At this point, we can (hopefully) easily manipulate the stylesheet to change the colors.
Generating an IDA `.clr` file should be an easy step of mapping the stylesheet back to a `.clr` file.

## Current status

UBER HACK

The initial view generation kinda works.
Next step is the UI.

## Common Pitfalls

1. IDA uses BGR for colors, not RGB.