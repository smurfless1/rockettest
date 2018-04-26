# rockettest

Simple-ish command line cart calculator with some discount processing.
I had way too much fun with the prompt toolkit.

## Usage

```
docker build -t cart .
docker run -it --rm --name cart cart
```

Because I know where to find bash on my mac, I also included the helper scripts build.sh and run.sh. Used together, they keep me from having to remember things.

Once you have it running, you'll get this little blob of text (or something similar):

```
===============================================================================
General notes: Tab completion works, and type exit to return cleanly.
You can use commas between codes if you like, but at least a space is required.
The code 'clear' will empty your cart.
Including the code 'exit' will stop after the next cart list.
===============================================================================
```

After adding some things to your cart, you might find discounts being applied:

```
Basket: AP1 AP1 AP1 MK1
Item                          Price
----                          -----
AP1                           $6.00
            AAPL             -$1.50
AP1                           $6.00
            AAPL             -$1.50
AP1                           $6.00
            AAPL             -$1.50
MK1                           $4.75
-----------------------------------
                             $18.25
```

If you decide you need fewer apples in your world after all: `clear` should clear it out for you. `exit` will finish adding things, print your total, and exit. You can also use ctrl-c or ctrl-d to exit.

