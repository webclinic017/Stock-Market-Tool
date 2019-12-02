import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'app-about',
    template: `
        <div class="container">
            <div class="gray-box">
                <h2>Stock Market Valuations</h2>
                <h4>the Power of Value Investing</h4>
                <p>
                    This website is designed to empower <em>you</em> with the knowledge required to be a smart,
                    successful value-investor. What is value investing? Value Investing is built on the idea that
                    many companies are being traded for a price that is less than, or in some cases greater than,
                    their true intrinsic value. A value investor will determine this intrinsic value to the best of
                    their ability, and then choose to buy or sell relative to whether or not the value is higher
                    or lower than the current trading price. This works because the theory surrounding this method
                    suggests that actual trading price will enventually rise or fall to meet intrinsic value.
                </p>
            </div>
            <div class="smt-row">
                <div class="gray-box">
                    <h3>How is a Stock Intrinsically Valued?</h3>
                    <p>
                        The valuation method used by this web application to intrinsically value a stock follows
                        the formular presented here to the right. This intrinsic formula was developed by famed investor and
                        scholar Benjamin Graham. Here, EPS refers to earning per share, PE to fair Rate of Return for a no
                        growth stock, g to growth rate of a company's earnings, gr to some coefficient for that growth, 4.4 to
                        the required return, and Y to AAA yield. <br /><br />
                    </p>
                </div>
                <div class="pic">
                    <img src="./formula.png" alt="forumla" width="250rem" height="80rem">
                </div>
            </div>
        </div>
    `,
    styleUrls: ['./about.component.scss']
})
export class AboutComponent implements OnInit {

    ngOnInit() {}

}
