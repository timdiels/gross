# Copyright (C) 2017 Tim Diels <timdiels.m@gmail.com>
#
# This file is part of Hyppo.
#
# Hyppo is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hyppo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Hyppo.  If not, see <http://www.gnu.org/licenses/>.

from kivy.app import App
from kivy.uix.widget import Widget

class PongGame(Widget):
    pass

class GrossApp(App):
    def build(self):
        return PongGame()

def main():
    GrossApp().run()

if __name__ == '__main__':
    main()
