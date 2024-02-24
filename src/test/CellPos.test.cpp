#include <catch2/catch_test_macros.hpp>

#include "../main/GameLogic.cpp"

TEST_CASE("should move on the same side", "[test]")
{
    CellPos pos = {Side::FRONT, 1, 1};
    CellPos up = pos.moveClone(Direction::UP);
    CellPos down = pos.moveClone(Direction::DOWN);
    CellPos left = pos.moveClone(Direction::LEFT);
    CellPos right = pos.moveClone(Direction::RIGHT);

    REQUIRE(up.side == Side::FRONT);
    REQUIRE(up.x == 1);
    REQUIRE(up.y == 2);

    REQUIRE(down.side == Side::FRONT);
    REQUIRE(down.x == 1);
    REQUIRE(down.y == 0);

    REQUIRE(left.side == Side::FRONT);
    REQUIRE(left.x == 0);
    REQUIRE(left.y == 1);

    REQUIRE(right.side == Side::FRONT);
    REQUIRE(right.x == 2);
    REQUIRE(right.y == 1);
}

TEST_CASE("Should stop at borders", "[test]")
{
    CellPos down = (CellPos){Side::FRONT, 0, 0}.moveClone(Direction::DOWN);
    CellPos up = (CellPos){Side::TOP, 0, SIZE}.moveClone(Direction::UP);
    CellPos left = (CellPos){Side::LEFT, 0, 0}.moveClone(Direction::LEFT);
    CellPos right = (CellPos){Side::RIGHT, SIZE, 0}.moveClone(Direction::RIGHT);

    REQUIRE(down.side == Side::FRONT);
    REQUIRE(down.x == 0);
    REQUIRE(down.y == 0);

    REQUIRE(up.side == Side::TOP);
    REQUIRE(up.x == 0);
    REQUIRE(up.y == SIZE);

    REQUIRE(left.side == Side::LEFT);
    REQUIRE(left.x == 0);
    REQUIRE(left.y == 0);

    REQUIRE(right.side == Side::RIGHT);
    REQUIRE(right.x == SIZE);
    REQUIRE(right.y == 0);
}

TEST_CASE("Should switch sides", "[test]")
{

    CellPos topDown = (CellPos){Side::TOP, 0, 0}.moveClone(Direction::DOWN);
    REQUIRE(topDown.side == Side::FRONT);
    REQUIRE(topDown.x == 0);
    REQUIRE(topDown.y == SIZE - 1);

    CellPos topLeft = (CellPos){Side::TOP, 0, 0}.moveClone(Direction::LEFT);
    REQUIRE(topLeft.side == Side::LEFT);
    REQUIRE(topLeft.x == SIZE - 1);
    REQUIRE(topLeft.y == SIZE - 1);

    CellPos topRight = (CellPos){Side::TOP, SIZE - 1, 0}.moveClone(Direction::RIGHT);
    REQUIRE(topRight.side == Side::RIGHT);
    REQUIRE(topRight.x == 0);
    REQUIRE(topRight.y == SIZE - 1);

    CellPos frontUp = (CellPos){Side::FRONT, 0, SIZE - 1}.moveClone(Direction::UP);
    REQUIRE(frontUp.side == Side::TOP);
    REQUIRE(frontUp.x == 0);
    REQUIRE(frontUp.y == 0);

    CellPos frontLeft = (CellPos){Side::FRONT, 0, 0}.moveClone(Direction::LEFT);
    REQUIRE(frontLeft.side == Side::LEFT);
    REQUIRE(frontLeft.x == SIZE - 1);
    REQUIRE(frontLeft.y == 0);

    CellPos frontRight = (CellPos){Side::FRONT, SIZE - 1, 0}.moveClone(Direction::RIGHT);
    REQUIRE(frontRight.side == Side::RIGHT);
    REQUIRE(frontRight.x == 0);
    REQUIRE(frontRight.y == 0);

    CellPos leftUp = (CellPos){Side::LEFT, 0, SIZE - 1}.moveClone(Direction::UP);
    REQUIRE(leftUp.side == Side::TOP);
    REQUIRE(leftUp.x == 0);
    REQUIRE(leftUp.y == SIZE - 1);

    CellPos leftRight = (CellPos){Side::LEFT, SIZE - 1, 0}.moveClone(Direction::RIGHT);
    REQUIRE(leftRight.side == Side::FRONT);
    REQUIRE(leftRight.x == 0);
    REQUIRE(leftRight.y == 0);

    CellPos rightUp = (CellPos){Side::RIGHT, 0, SIZE - 1}.moveClone(Direction::UP);
    REQUIRE(rightUp.side == Side::TOP);
    REQUIRE(rightUp.x == SIZE - 1);
    REQUIRE(rightUp.y == 0);

    CellPos rightLeft = (CellPos){Side::RIGHT, 0, 0}.moveClone(Direction::LEFT);
    REQUIRE(rightLeft.side == Side::FRONT);
    REQUIRE(rightLeft.x == SIZE - 1);
    REQUIRE(rightLeft.y == 0);
}