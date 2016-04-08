#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 11 Synthesizing Tasks."""

import time

board='abcdefgh'


class ChessPiece( object ):
        def __init__(self, position):
            #print("In const")
            self.position = ''
            self.prefix = ''
            self.moves = []
            try:
                if self.is_legal_move(position):
                  self.position = position
                  self.prefix = ''
                  self.moves = []
                else:
                  raise ValueError("test")
            except:
                excep = '`{}` is not a legal start position'
                raise ValueError(excep.format(position))


        def is_legal_move(self, pos):
            #print("In is_legal_move")
            value = False
            data = self.algebraic_to_numeric(pos)
            #print("Data {0}".format(data))
            if data is None:
                value =  False
            elif data[0] <= 7 and data[1] <= 7:
                value = True
            else:
                value = False
             #print(" Return value {0}".format(value))
            return value


        def algebraic_to_numeric(self, pos):
            #print("In algebraic_to_numeric {0}".format(pos))
            
            try:
                a1 = board.index(pos[:1].lower())
                a2 = int(pos[1:2])
                #print("a1 = {0}, a2 = {1}".format(a1, a2))
                if a1 <= 7 and a2 <= 8:
                #print("return = {0}".format((a1, a2-1)))
                    return (a1, a2-1)
                else:
                #print (None)
                 return None 
            except:
                #print (None)
                return None


        def move(self,pos):
            try:
                    if self.is_legal_move(pos):
                       #print(" value {0}{1}{2}".format(self.prefix,self.position,pos))
                       m = ("{0}{1}".format(self.prefix,self.position),"{0}{1}".format(self.prefix,pos),time.time())
                       self.moves.append(m)
                       self.position = pos
                       return m
                    else:
                        return False
            except:
                    return False


class Rook(ChessPiece):
      def __init__(self, position):
        #super(self.__class__, self).__init__(position)
        ChessPiece.__init__(self, position)
        self.prefix = 'R'


      def is_legal_move(self,pos):
          #print(" Called with pos {0} ".format(self.position))
          data = super(self.__class__, self).is_legal_move(pos)
          #print(" Called with pos {0} ".format(self.position))
          if self.position=='':
             #print(" In If")
             return data
          else:
              #print("In else")
              data1 = self.algebraic_to_numeric(pos)
              #print("data1 = {0}".format(data1))
              p1 = board.index(self.position[:1].lower())
              #print("p1 = {0} ".format(p1))
              p2 = int(self.position[1:2])
              #print("p2 = {0} ".format(p2))
              #print("data = {0}".format(data))
              if data is True and ( p1 == data1[0] or p2 == data1[1]+1):
                 return True
              else:
                 return False


class Bishop(ChessPiece):
      def __init__(self, position):
        #super(self.__class__, self).__init__(position)
        ChessPiece.__init__(self,position)
        self.prefix = 'B'


      def is_legal_move(self, pos):
          #print(" Called with pos {0} ".format(self.position))
          data = super(self.__class__, self).is_legal_move(pos)
          #print(" Called with pos {0} ".format(self.position))
          if self.position == '':
             #print(" In If")
             return data
          else:
              #print("In else")
              data1 = self.algebraic_to_numeric(pos)
              #print("data1 = {0}".format(data1))
              p1 = board.index(self.position[:1].lower())
              #print("p1 = {0} ".format(p1))
              p2 = int(self.position[1:2])-1
              #print("p2 = {0} ".format(p2))
              print("data = {0}".format(data))
              if data == True and abs(p1 - data1[0]) == abs(p2 - data1[1]):
                 return True
              else:
                 return False


class King(ChessPiece):
      def __init__(self, position):
        #super(self.__class__, self).__init__(position)
        ChessPiece.__init__(self, position)
        self.prefix = 'K'


      def is_legal_move(self,pos):
          #print(" Called with pos {0} ".format(self.position))
          data = super(self.__class__, self).is_legal_move(pos)
          #print(" Called with pos {0} ".format(self.position))
          if self.position == '':
            #print(" In If")
            return data
          else:
            #print("In else")
            data1 = self.algebraic_to_numeric(pos)
            #print("data1 = {0}".format(data1))
            p1 = board.index(self.position[:1].lower())
            #print("p1 = {0} ".format(p1))
            p2 = int(self.position[1:2])-1
            #print("p2 = {0} ".format(p2))
            #print("data = {0}".format(data))
            if data == True and ((abs(p1 - data1[0]) == 1
            and abs(p2 - data1[1]) == 1) or (abs(p1 - data1[0]) == 0
            and abs(p2 - data1[1]) == 1) or (abs(p1 - data1[0]) == 1
            and abs(p2 - data1[1]) == 0)):
                 return True
            else:
                  return False


class ChessMatch(object):
        def __init__(self, pieces=None):
                self.pieces = pieces
                self.log = []


        def reset(self):
                self.log = []

                self.pieces ={
                    'Ra1':Rook('a1'),
                    'Rh1':Rook('h1'),
                    'Ra8':Rook('a8'),
                    'Rh8':Rook('h8'),
                    'Bc1':Bishop('c1'),
                    'Bf1':Bishop('f1'),
                    'Bc8':Bishop('c8'),
                    'Bf8':Bishop('f8'),
                    'Ke1':King('e1'),
                    'Ke8':King('e8')
                        }


        def move(self, p, m):
            match.pieces.get(p)
            nm = self.pieces.get(p).move(m)
            pref = self.pieces.get(p).prefix
            if nm != False:
                self.log.append(nm)
                del self.pieces[p]
            if  pref == 'K':
                match.pieces["K{0}".format(m)] = King(m)
            if pref == 'R':
                match.pieces["R{0}".format(m)] = Rook(m)
            if pref == 'B':
                match.pieces["B{0}".format(m)] = Bishop(m)
