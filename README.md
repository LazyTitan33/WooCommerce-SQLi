# CVE-2021-32790

This is a Proof of Concept for the <i>WooCommerce 3.3-5.5 Blind Time based SQL Injection</i> written quickly in python3. 

In my case it was Unauthenticated but if yours require authentication, make sure to add the cookies in the script and it should still work. When adding the URL as an argument, you will see the response time. Default script has a sleep of 5 seconds. Feel free to adjust as needed.

![image](https://user-images.githubusercontent.com/80063008/150332148-3ed70d14-af57-4d06-86f3-1c704e071fc0.png)

![image](https://user-images.githubusercontent.com/80063008/150332835-24361d49-bc21-45c0-8182-7aae78ef6982.png)


For the inspiration, special thanks go to [@zeroauth](https://twitter.com/intent/follow?ref_src=twsrc%5Etfw%7Ctwcamp%5Ebuttonembed%7Ctwterm%5Efollow%7Ctwgr%5Ezeroauth&screen_name=zeroauth) who wrote the sqlmap tamper script below.

https://zeroauth.ltd/blog/2021/07/16/proof-of-concept-exploit-for-woocommerce-3-3-5-5-sql-injection-with-sqlmap-tamper/
