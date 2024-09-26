#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2021 LG Electronics Inc.
# SPDX-License-Identifier: Apache-2.0

UBUNTU_COMMANDS = [
    "fosslight_dependency -p tests/test_maven1/lombok.maven -o tests/result/maven1",
    "fosslight_dependency -p tests/test_maven2 -o tests/result/maven2"
]


def test_ubuntu(run_command):
    for command in UBUNTU_COMMANDS:
        return_code, stdout, stderr = run_command(command)
        assert return_code == 0, f"Command failed: {command}\nstdout: {stdout}\nstderr: {stderr}"
