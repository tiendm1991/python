class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = {0: homepage}
        self._max = 0
        self._current = 0

    def visit(self, url: str) -> None:
        self._current += 1
        if self._current not in self.history or self.history[self._current] != url:
            self._max = self._current
            self.history[self._current] = url

    def back(self, steps: int) -> str:
        if self._current - steps < 0:
            self._current = 0
            return self.history[0]
        self._current -= steps
        return self.history[self._current]

    def forward(self, steps: int) -> str:
        if self._current + steps > self._max:
            self._current = self._max
            return self.history[self._max]
        self._current += steps
        return self.history[self._current]


browserHistory = BrowserHistory("momn.com")
browserHistory.visit("bx.com")
browserHistory.visit("bjyfmln.com")
print(browserHistory.back(3))
browserHistory.visit("ijtrqk.com")
browserHistory.visit("dft.com")
browserHistory.visit("gtd.com")
print(browserHistory.back(3))
